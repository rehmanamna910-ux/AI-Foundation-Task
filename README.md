# Guardrailed RAG System with FastAPI & Vector Search

A production-ready Retrieval-Augmented Generation (RAG) backend API built with Python, FastAPI, and Sentence-Transformers (`all-MiniLM-L6-v2`). Includes risk guardrails against hallucinations and strict Pydantic input validation.

## Architecture & Features
**Semantic Retrieval:** Uses vector embeddings and cosine similarity to match user queries with relevant document context.
**RESTful API:** Powered by FastAPI for fast, asynchronous endpoint delivery.
**Risk Guardrails:** Implements similarity threshold checks to prevent hallucinated or out-of-context answers.
**Input Validation:** Enforces strict payload validation (minimum query length constraints) to return `422 Unprocessable Entity` for malformed inputs.

## Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/rehmanamna910-ux/AI-Foundation-Task.git](https://github.com/rehmanamna910-ux/AI-Foundation-Task.git)
   cd AI-Foundation-Task
Activate Virtual Environment:

PowerShell
.\venv\Scripts\activate
Install Dependencies:

Bash
pip install fastapi uvicorn sentence-transformers requests pydantic
Running the Project (Week 7 Integration Flow)
Start the FastAPI Server:

PowerShell
cd "Week 7"
..\venv\Scripts\python.exe -m uvicorn main:app --reload
Execute Client Integration Demo:

PowerShell
# Open a new terminal tab
cd "Week 7"
..\venv\Scripts\python.exe client_demo.py
API Endpoints
POST /query: Processes user query, computes similarity scores, and returns context-backed answers or triggers security guardrails.

Known Limitations & Assumptions
Static Context: Uses local document chunking rather than a distributed vector database like Pinecone or ChromaDB.

Local Model Execution: Embeddings are generated locally on CPU, which can be migrated to GPU or cloud API services for higher throughput.