import math
from sentence_transformers import SentenceTransformer


class RAGEngine:

  def __init__(self, doc_path: str, threshold: float = 0.35):
    self.threshold = threshold
    self.model = SentenceTransformer("all-MiniLM-L6-v2")

    # Load and chunk document
    with open(doc_path, "r", encoding="utf-8") as f:
      text = f.read()

    # Simple character chunking
    chunk_size = 200
    self.chunks = [
        text[i : i + chunk_size] for i in range(0, len(text), chunk_size - 50)
    ]
    self.embeddings = self.model.encode(self.chunks)

  def cosine_similarity(self, vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_a = math.sqrt(sum(a * a for a in vec1))
    norm_b = math.sqrt(sum(b * b for b in vec2))
    if norm_a == 0 or norm_b == 0:
      return 0.0
    return dot_product / (norm_a * norm_b)

  def search(self, query: str):
    query_emb = self.model.encode(query)
    best_score = -1.0
    best_chunk = ""

    for chunk, emb in zip(self.chunks, self.embeddings):
      score = self.cosine_similarity(query_emb, emb)
      if score > best_score:
        best_score = score
        best_chunk = chunk

    # Security & Hallucination Guardrail Check
    if best_score < self.threshold:
      return {
          "found": False,
          "answer": (
              "[Risk Guardrail Alert] Relevant information not found in context"
              " to prevent hallucination."
          ),
          "score": float(best_score),
      }

    return {"found": True, "answer": best_chunk.strip(), "score": float(best_score)}