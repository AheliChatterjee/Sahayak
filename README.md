# Agentic Enterprise Assistant

A reliability-first AI assistant that combines Retrieval-Augmented Generation (RAG) with lightweight agentic routing to answer enterprise document queries with page-level citations and generate structured JSON outputs for workflow automation commands.

---

## Key Features

* Citation-grounded document question answering
* Hallucination guardrails for safe responses
* Intent-based routing between information and action modes
* Deterministic JSON outputs for enterprise workflows
* Simple Streamlit-based user interface

---

## Tech Stack

* **Backend:** FastAPI
* **UI:** Streamlit
* **PDF Parsing:** PyPDF
* **Chunking:** LangChain Text Splitters
* **Embeddings:** sentence-transformers/all-MiniLM-L6-v2
* **Vector Database:** ChromaDB
* **LLM:** Hugging Face Inference API (meta-Llama-3-8B-instruct)
* **Agent Logic:** Custom Python routing

---

## Project Structure

```
agentic-enterprise-assistant/
├── app.py                 # Streamlit UI
|__main.py                 # FastAPI backend Entry  point
├── requirements.txt       # Dependencies
├── data/                  # PDF documents
├── ingestion/             # PDF loading and chunking
├── rag/                   # Vector store and RAG pipeline
├── agent/                 # Intent router and controller
├── actions/               # Action prompts and handlers
└── README.md              # Project documentation
```

---

## Setup

1. Clone the repository
git clone <https://github.com/AheliChatterjee/Sahayak>
cd agentic-enterprise-assistant

2. Create virtual environment
python -m venv venv

Activate:

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add Hugging Face Token

Set environment variable:

HF_TOKEN=<your_huggingface_token>

## Running the Application

Run Backend API
uvicorn main:app

Backend will start at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

## Run Streamlit UI (Optional)

streamlit run app.py
API Endpoint
Chat Endpoint
POST /chat
Request
{
  "query": "What are the key risks mentioned in the report?"
}
Response
{
  "response": "Generated answer from RAG pipeline"
}

---

## System Architecture
```

                ┌──────────────────────┐
                │      Frontend        │
                │ (Streamlit / Web UI) │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │      FastAPI API     │
                │       /chat          │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Agent Controller  │
                │  (Intent Routing)    │
                └───────┬────────┬─────┘
                        │        │
                        ▼        ▼
                ┌────────────┐ ┌─────────────┐
                │   RAG Mode │ │ Action Mode │
                │ Doc Search │ │ JSON Output │
                └──────┬─────┘ └──────┬──────┘
                       │              │
                       ▼              ▼
             ┌────────────────┐ ┌───────────────┐
             │ Chroma Vector  │ │ Llama-3 LLM   │
             │ Database       │ │ Inference API │
             └──────┬─────────┘ └──────┬────────┘
                    │ Retrieved Docs    │
                    ▼                   ▼
          ┌─────────────────────────────────┐
          │ Citation-Grounded Answer OR    │
          │ Deterministic Action JSON      │
          └─────────────────────────────────┘
          
```

## How It Works

1. User submits a query via UI or API
2. Intent router classifies query:

   * Informational → RAG pipeline
   * Action → JSON action generator
3. RAG retrieves relevant document chunks from ChromaDB
4. LLM generates citation-grounded response
5. Action requests return structured JSON

---

## Demo Queries

### Document Queries

* What are the key risks mentioned in the report?
* What initiatives are mentioned for digital transformation?

### Action Commands

* Schedule a meeting with HR tomorrow at 3 PM
* Create an IT ticket for laptop not turning on, high priority

### Hallucination Guardrail

* Who is the CEO of Google?

---

## Output Examples

### Citation-Grounded Answer

"The report identifies key risks including global economic uncertainty and market volatility, discussed on Pages 45 and 46."

### Action JSON

```
{
  "action": "create_it_ticket",
  "issue": "Laptop not turning on",
  "priority": "High"
}
```

---

## Conclusion

The Agentic Enterprise Assistant demonstrates an enterprise-ready AI system that ensures accuracy, transparency, and deterministic automation through RAG and agentic control.
