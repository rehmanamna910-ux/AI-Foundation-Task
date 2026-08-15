import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def chunk_text(text: str, chunk_size: int = 40, overlap: int = 10):
    words = text.split()
    step = chunk_size - overlap
    return [
        " ".join(words[i : i + chunk_size])
        for i in range(0, len(words), step)
        if words[i : i + chunk_size]
    ]


class RAGEngine:
    def __init__(self, doc_path: str, threshold: float = 0.35):
        self.threshold = threshold

        # Document read karna
        with open(doc_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Chunks banana
        self.chunks = chunk_text(text)

        # Model sirf ek baar server start hone par load hoga
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.chunk_embeddings = self.embedder.encode(self.chunks)

    def query(self, question: str):
        query_emb = self.embedder.encode([question])
        scores = cosine_similarity(query_emb, self.chunk_embeddings)[0]

        best_idx = int(np.argmax(scores))
        best_score = float(scores[best_idx])

        if best_score < self.threshold:
            return {
                "found": False,
                "answer": "Relevant context not found to prevent hallucination.",
                "score": best_score,
            }

        return {
            "found": True,
            "answer": self.chunks[best_idx],
            "score": best_score,
        }