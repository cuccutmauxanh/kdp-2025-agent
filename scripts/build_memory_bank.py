"""
Script xây dựng Memory-Bank vectorstore từ các research note trong vault
Sử dụng ChromaDB để lưu trữ embedding vector
"""

import os
from pathlib import Path
from chromadb import Client
from chromadb.config import Settings
from chromadb.utils import embedding_functions

VAULT_PATH = Path("vault/01-LEARNING/01-Research-Projects")
VECTOR_DB_PATH = "memory_bank/chroma_db"

# Tạo thư mục lưu vectorstore nếu chưa có
os.makedirs(VECTOR_DB_PATH, exist_ok=True)

# Khởi tạo ChromaDB client
client = Client(Settings(
    persist_directory=VECTOR_DB_PATH
))

# Sử dụng embedding function mặc định (OpenAI hoặc sentence-transformers)
def get_embedding_function():
    # Nếu bạn có API key OpenAI, có thể dùng OpenAIEmbeddingFunction
    # return embedding_functions.OpenAIEmbeddingFunction(api_key="sk-xxx")
    # Dùng sentence-transformers (miễn phí, local)
    return embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

embedding_fn = get_embedding_function()

# Tạo collection cho research notes
collection = client.get_or_create_collection(
    name="research_notes",
    embedding_function=embedding_fn
)

def ingest_notes():
    docs = []
    metadatas = []
    ids = []
    for project_dir in VAULT_PATH.iterdir():
        overview_path = project_dir / "Overview.md"
        if overview_path.exists():
            with open(overview_path, "r", encoding="utf-8") as f:
                content = f.read()
                doc_id = f"{project_dir.name}-overview"
                docs.append(content)
                metadatas.append({"project": project_dir.name, "type": "overview"})
                ids.append(doc_id)
    print(f"Đã tìm thấy {len(docs)} research notes để ingest vào vectorstore.")
    if docs:
        collection.add(
            documents=docs,
            metadatas=metadatas,
            ids=ids
        )
        print("✅ Đã ingest research notes vào Memory-Bank (ChromaDB)")
    else:
        print("⚠️ Không tìm thấy research notes nào để ingest.")

def main():
    ingest_notes()
    client.persist()
    print(f"✅ Đã lưu vectorstore vào {VECTOR_DB_PATH}")

if __name__ == "__main__":
    main() 