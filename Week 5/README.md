# Week 5: Mini RAG Service API

This directory contains the production-ready FastAPI web service for the Retrieval-Augmented Generation (RAG) system built during Week 5. It transitions the local Python script into a reusable API endpoint.

## Project Structure
- `main.py` - FastAPI app initialization, logging configuration, and `/query` endpoint definition.
- `rag_core.py` - Core RAG engine handling document loading, vector embeddings, and cosine similarity search.
- `sample_document.txt` - Healthcare knowledge base document (Stroke Types, Risk Factors, and Guidelines).
- `requirements.txt` - Project dependencies.

## Features & Implementation
- **Framework**: FastAPI with Uvicorn server.
- **Validation**: Pydantic models (`QueryRequest`, `QueryResponse`) for strict request/response schemas.
- **Embeddings**: `sentence-transformers` (`all-MiniLM-L6-v2`) for vector search.
- **Documentation**: Automatic interactive API docs generated via Swagger UI.

## How to Run & Test

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
Start the FastAPI Server:

Bash
uvicorn main:app --reload
Test via Interactive Swagger UI:

Open browser and navigate to: http://127.0.0.1:8000/docs

Expand the POST /query endpoint and click Try it out.

Input the sample query payload:

JSON
{
  "question": "What is stroke and what are its types?"
}
Click Execute to view the similarity score and extracted answer