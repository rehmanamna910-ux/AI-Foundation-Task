import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from rag_core import RAGEngine

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("rag-api-week6")

app = FastAPI(title="Week 6 Secure RAG API")

# Initialize RAG Engine
engine = RAGEngine("sample_document.txt", threshold=0.35)


# Input Validation Schema (Safety Guardrail)
class QueryRequest(BaseModel):
  query: str = Field(
      ...,
      min_length=3,
      max_length=300,
      description="Query must be between 3 and 300 characters.",
  )


@app.post("/query")
def process_query(request: QueryRequest):
  logger.info(f"Received query: '{request.query}'")

  # Run RAG search
  result = engine.search(request.query)

  # Check if confidence threshold passed
  if not result["found"]:
    logger.warning(
        f"Low score or irrelevant query detected for: '{request.query}'"
    )

  return result