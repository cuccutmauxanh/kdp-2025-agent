"""
Build Memory Bank - Xây dựng ChromaDB từ Obsidian Vault
======================================================

Script này sẽ đọc tất cả notes từ Obsidian Vault và tạo ChromaDB collection
để AI agent có thể query knowledge một cách hiệu quả.
"""

import chromadb
import json
import logging
from pathlib import Path
from typing import List, Dict, Any
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MemoryBankBuilder:
    """
    Builder để tạo ChromaDB Memory Bank từ Obsidian Vault
    """
    
    def __init__(self, vault_path: str = "vault", db_path: str = "data/memory_bank"):
        """
        Khởi tạo Memory Bank Builder
        
        Args:
            vault_path: Đường dẫn đến Obsidian Vault
            db_path: Đường dẫn đến ChromaDB
        """
        self.vault_path = Path(vault_path)
        self.db_path = Path(db_path)
        self.client = None
        self.collection = None
        
        # Tạo thư mục nếu chưa có
        self.db_path.mkdir(parents=True, exist_ok=True)
        
        logger.info("🏗️ Memory Bank Builder đã được khởi tạo")
    
    def connect_to_chromadb(self) -> None:
        """Kết nối với ChromaDB"""
        try:
            self.client = chromadb.PersistentClient(path=str(self.db_path))
            logger.info("✅ Đã kết nối với ChromaDB")
        except Exception as e:
            logger.error(f"❌ Lỗi kết nối ChromaDB: {e}")
            raise
    
    def create_or_get_collection(self, collection_name: str = "kdp_knowledge") -> None:
        """Tạo hoặc lấy collection"""
        try:
            # Thử lấy collection hiện có
            self.collection = self.client.get_collection(collection_name)
            logger.info(f"📂 Đã lấy collection: {collection_name}")
        except:
            # Tạo collection mới
            self.collection = self.client.create_collection(
                name=collection_name,
                metadata={"description": "KDP 2025 Knowledge Base"}
            )
            logger.info(f"🆕 Đã tạo collection mới: {collection_name}")
    
    def read_markdown_files(self) -> List[Dict[str, Any]]:
        """
        Đọc tất cả markdown files từ vault
        
        Returns:
            List các documents với metadata
        """
        documents = []
        
        # Tìm tất cả .md files
        md_files = list(self.vault_path.rglob("*.md"))
        logger.info(f"📁 Tìm thấy {len(md_files)} markdown files")
        
        for file_path in md_files:
            try:
                # Đọc content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Tạo metadata
                relative_path = file_path.relative_to(self.vault_path)
                metadata = {
                    "source": str(relative_path),
                    "file_type": "markdown",
                    "category": self._get_category_from_path(relative_path),
                    "size": len(content)
                }
                
                # Tách content thành chunks nhỏ hơn
                chunks = self._split_content(content, max_length=1000)
                
                for i, chunk in enumerate(chunks):
                    doc_id = f"{relative_path}_{i}"
                    documents.append({
                        "id": doc_id,
                        "content": chunk,
                        "metadata": {**metadata, "chunk_index": i}
                    })
                
                logger.info(f"📄 Đã xử lý: {relative_path} -> {len(chunks)} chunks")
                
            except Exception as e:
                logger.error(f"❌ Lỗi đọc file {file_path}: {e}")
        
        return documents
    
    def _get_category_from_path(self, relative_path: Path) -> str:
        """Lấy category từ đường dẫn file"""
        parts = relative_path.parts
        
        if len(parts) == 0:
            return "root"
        
        # Map folder names to categories
        category_map = {
            "00-META": "meta",
            "01-RESEARCH": "research", 
            "02-PLANNING": "planning",
            "03-DEVELOPMENT": "development",
            "04-TOOLS": "tools"
        }
        
        return category_map.get(parts[0], "other")
    
    def _split_content(self, content: str, max_length: int = 1000) -> List[str]:
        """
        Tách content thành các chunks nhỏ hơn
        
        Args:
            content: Content gốc
            max_length: Độ dài tối đa mỗi chunk
            
        Returns:
            List các chunks
        """
        if len(content) <= max_length:
            return [content]
        
        chunks = []
        current_chunk = ""
        
        # Tách theo paragraphs
        paragraphs = content.split('\n\n')
        
        for paragraph in paragraphs:
            if len(current_chunk) + len(paragraph) > max_length:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph
            else:
                current_chunk += "\n\n" + paragraph if current_chunk else paragraph
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def ingest_documents(self, documents: List[Dict[str, Any]]) -> None:
        """
        Ingest documents vào ChromaDB
        
        Args:
            documents: List documents cần ingest
        """
        if not documents:
            logger.warning("⚠️ Không có documents để ingest")
            return
        
        try:
            # Chuẩn bị data
            ids = [doc["id"] for doc in documents]
            contents = [doc["content"] for doc in documents]
            metadatas = [doc["metadata"] for doc in documents]
            
            # Ingest vào collection
            self.collection.add(
                ids=ids,
                documents=contents,
                metadatas=metadatas
            )
            
            logger.info(f"✅ Đã ingest {len(documents)} documents vào ChromaDB")
            
        except Exception as e:
            logger.error(f"❌ Lỗi ingest documents: {e}")
            raise
    
    def build_memory_bank(self) -> Dict[str, Any]:
        """
        Xây dựng toàn bộ Memory Bank
        
        Returns:
            Dict chứa thống kê
        """
        logger.info("🚀 Bắt đầu xây dựng Memory Bank...")
        
        # Kết nối ChromaDB
        self.connect_to_chromadb()
        
        # Tạo collection
        self.create_or_get_collection()
        
        # Đọc documents
        documents = self.read_markdown_files()
        
        # Ingest documents
        self.ingest_documents(documents)
        
        # Lấy thống kê
        stats = self.get_stats()
        
        logger.info("🎉 Hoàn thành xây dựng Memory Bank!")
        return stats
    
    def get_stats(self) -> Dict[str, Any]:
        """Lấy thống kê về Memory Bank"""
        try:
            count = self.collection.count()
            return {
                "total_documents": count,
                "collection_name": "kdp_knowledge",
                "db_path": str(self.db_path),
                "vault_path": str(self.vault_path),
                "status": "ready"
            }
        except Exception as e:
            return {"error": f"Lỗi lấy stats: {e}"}


def main():
    """Main function"""
    builder = MemoryBankBuilder()
    
    try:
        stats = builder.build_memory_bank()
        print("\n📊 Memory Bank Statistics:")
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        
    except Exception as e:
        logger.error(f"❌ Lỗi xây dựng Memory Bank: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main()) 