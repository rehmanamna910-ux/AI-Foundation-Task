import logging
from fastapi import FastAPI
from pydantic import BaseModel
from rag_core import RAGEngine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("rag-api")

app = FastAPI(title="Mini RAG Service API - Week 5")

logger.info("RAG Engine load ho raha hai...")
engine = RAGEngine("sample_document.txt", threshold=0.35)
logger.info("RAG Engine successfully load ho gaya!")


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    found: bool
    answer: str
    score: float


@app.get("/")
def home():
    return {"status": "online", "message": "RAG API Service active hai!"}


@app.post("/query", response_model=QueryResponse)
def handle_query(req: QueryRequest):
    logger.info(f"Incoming Question: '{req.question}'")

    result = engine.query(req.question)

    logger.info(f"Score: {result['score']:.4f} | Found: {result['found']}")

    return QueryResponse(
        found=result["found"],
        answer=result["answer"],
        score=result["score"]
    )