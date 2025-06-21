"""
Memory Query Tool - Tích hợp với ChromaDB Memory Bank
====================================================

Tool này cho phép AI agent query knowledge từ ChromaDB memory bank
để tìm kiếm thông tin liên quan từ các research documents đã ingest.
"""

import chromadb
import json
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MemoryQueryTool:
    """
    Tool để query knowledge từ ChromaDB Memory Bank
    
    Chức năng:
    1. Kết nối với ChromaDB
    2. Tìm kiếm documents liên quan
    3. Trả về context cho AI agent
    """
    
    def __init__(self, db_path: str = "data/memory_bank"):
        """
        Khởi tạo Memory Query Tool
        
        Args:
            db_path: Đường dẫn đến ChromaDB
        """
        self.db_path = db_path
        self.client = None
        self.collection = None
        self._connect_to_db()
        
        logger.info("🔍 Memory Query Tool đã được khởi tạo")
    
    def _connect_to_db(self) -> None:
        """Kết nối với ChromaDB"""
        try:
            self.client = chromadb.PersistentClient(path=self.db_path)
            self.collection = self.client.get_collection("kdp_knowledge")
            logger.info("✅ Đã kết nối với ChromaDB Memory Bank")
        except Exception as e:
            logger.error(f"❌ Lỗi kết nối ChromaDB: {e}")
            self.client = None
            self.collection = None
    
    def query_knowledge(self, query_text: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """
        Tìm kiếm knowledge liên quan
        
        Args:
            query_text: Text để tìm kiếm
            n_results: Số kết quả trả về
            
        Returns:
            List các documents liên quan
        """
        if not self.collection:
            logger.warning("⚠️ Chưa kết nối được với ChromaDB")
            return []
        
        try:
            # Query ChromaDB
            results = self.collection.query(
                query_texts=[query_text],
                n_results=n_results
            )
            
            # Format kết quả
            documents = []
            for i in range(len(results['documents'][0])):
                doc = {
                    'content': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                    'distance': results['distances'][0][i] if results['distances'] else 0.0,
                    'id': results['ids'][0][i] if results['ids'] else f"doc_{i}"
                }
                documents.append(doc)
            
            logger.info(f"🔍 Tìm thấy {len(documents)} documents liên quan")
            return documents
            
        except Exception as e:
            logger.error(f"❌ Lỗi query ChromaDB: {e}")
            return []
    
    def get_context_for_query(self, query_text: str, max_length: int = 2000) -> str:
        """
        Lấy context cho query từ memory bank
        
        Args:
            query_text: Query text
            max_length: Độ dài tối đa của context
            
        Returns:
            Context string
        """
        documents = self.query_knowledge(query_text, n_results=3)
        
        if not documents:
            return "Không tìm thấy thông tin liên quan trong memory bank."
        
        # Tạo context từ documents
        context_parts = []
        current_length = 0
        
        for doc in documents:
            content = doc['content']
            metadata = doc.get('metadata', {})
            source = metadata.get('source', 'Unknown')
            
            # Format document info
            doc_info = f"📄 Source: {source}\n{content}\n"
            
            if current_length + len(doc_info) > max_length:
                break
                
            context_parts.append(doc_info)
            current_length += len(doc_info)
        
        context = "\n---\n".join(context_parts)
        return context
    
    def search_by_topic(self, topic: str) -> List[Dict[str, Any]]:
        """
        Tìm kiếm theo topic cụ thể
        
        Args:
            topic: Topic cần tìm
            
        Returns:
            List documents liên quan đến topic
        """
        return self.query_knowledge(f"topic: {topic}", n_results=10)
    
    def search_by_repository(self, repo_name: str) -> List[Dict[str, Any]]:
        """
        Tìm kiếm documents từ repository cụ thể
        
        Args:
            repo_name: Tên repository
            
        Returns:
            List documents từ repo
        """
        if not self.collection:
            return []
        
        try:
            # Query với filter theo repo
            results = self.collection.query(
                query_texts=[""],
                n_results=50,
                where={"source": {"$contains": repo_name}}
            )
            
            documents = []
            for i in range(len(results['documents'][0])):
                doc = {
                    'content': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                    'id': results['ids'][0][i] if results['ids'] else f"doc_{i}"
                }
                documents.append(doc)
            
            return documents
            
        except Exception as e:
            logger.error(f"❌ Lỗi search by repository: {e}")
            return []
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """
        Lấy thống kê về memory bank
        
        Returns:
            Dict chứa thống kê
        """
        if not self.collection:
            return {"error": "Chưa kết nối với ChromaDB"}
        
        try:
            count = self.collection.count()
            return {
                "total_documents": count,
                "db_path": self.db_path,
                "collection_name": "kdp_knowledge",
                "status": "connected"
            }
        except Exception as e:
            return {"error": f"Lỗi lấy stats: {e}"}


def main():
    """Test function cho Memory Query Tool"""
    tool = MemoryQueryTool()
    
    # Test stats
    stats = tool.get_memory_stats()
    print("📊 Memory Bank Stats:")
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    
    # Test query
    query = "AI agent development"
    context = tool.get_context_for_query(query)
    print(f"\n🔍 Query: {query}")
    print(f"📄 Context: {context[:200]}...")
    
    # Test search by topic
    topic_docs = tool.search_by_topic("machine learning")
    print(f"\n📚 Documents về 'machine learning': {len(topic_docs)}")


if __name__ == "__main__":
    main() 