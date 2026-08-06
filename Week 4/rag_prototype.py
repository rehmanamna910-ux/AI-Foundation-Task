import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# 1. Load Document
doc_path = os.path.join("Week 4", "sample_document.txt")
if not os.path.exists(doc_path):
    doc_path = "sample_document.txt"

with open(doc_path, "r", encoding="utf-8") as f:
    full_text = f.read()

# 2. Document Chunking
def chunk_text(text, chunk_size=40, overlap=10):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks

chunks = chunk_text(full_text)
print(f"--- Document Chunking Complete: {len(chunks)} Chunks Created ---")

# 3. Embeddings Generation
embedder = SentenceTransformer('all-MiniLM-L6-v2')
chunk_embeddings = embedder.encode(chunks)
print("--- Vector Embeddings Generated Successfully ---")

# 4. Search & RAG Retrieval Function
def search_and_respond(query):
    query_emb = embedder.encode([query])
    scores = cosine_similarity(query_emb, chunk_embeddings)[0]
    best_idx = np.argmax(scores)
    best_score = scores[best_idx]
    
    print(f"\nUser Query: '{query}'")
    
    # Hallucination Threshold Guardrail
    if best_score < 0.35:
        print("Response: [Risk Management Alert] Information not found in context to prevent hallucination.")
        return
        
    print(f"Retrieved Chunk {best_idx + 1} (Score: {best_score:.4f}):")
    print(f"  \"{chunks[best_idx]}\"")
    print(f"RAG Generated Response (with Citation):")
    print(f"  Based on Healthcare Knowledge Base (Chunk {best_idx + 1}): {chunks[best_idx]}")

# 5. Testing Queries
if __name__ == "__main__":
    search_and_respond("What is the difference between Ischemic and Hemorrhagic stroke?")
    search_and_respond("What are the primary medical risk factors for stroke?")
    search_and_respond("Which machine learning models are used for stroke prediction?")
    search_and_respond("What is the refund policy for hospital bills?") # Hallucination test case