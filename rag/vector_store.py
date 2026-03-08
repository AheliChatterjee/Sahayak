import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

DB_PATH = os.path.join(os.getcwd(), "chroma_db")

def create_vector_store(chunks):
    client = chromadb.PersistentClient(
            path="DB_PATH"
        )
    
    
    collection_name = "hcltech_report"
    
    existing_collections = [c.name for c in client.list_collections()]
    
    if collection_name in existing_collections:
        print("Loading existing vector database...")
        collection = client.get_collection(name=collection_name)
        return collection

    print("Creating vector database...")
    
    collection = client.create_collection(
        name=collection_name
    )
    
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [c["text"] for c in chunks]
    metadatas = [{"page": c["page"]} for c in chunks]
    ids = [str(i) for i in range(len(chunks))]

    embeddings = embedder.encode(
        texts,
        show_progress_bar= True
        ).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    print("Saving vector database...")


    return collection

# Load Existing Vector Store
def load_vector_store():
    client = chromadb.PersistentClient(path=DB_PATH)
    
    collections = client.list_collections()

    print("Available collections:", collections)
    
    collection = client.get_collection(name="hcltech_report")

    print("Loaded existing vector database")

    return collection

