from ingestion.load_pdf import load_pdf_by_page
from ingestion.chunk_text import chunk_pages
from rag.vector_store import create_vector_store

print("Loading PDF...")
pages = load_pdf_by_page("data/Annual-Report-2024-25.pdf")

print("Chunking...")
chunks = chunk_pages(pages)

print("Creating vector store...")
create_vector_store(chunks)

print("Vector database saved successfully.")