# Week 8 Final System Verification & Test Notes

**Project Name:** Guardrailed RAG System with FastAPI & Vector Search  
**Prepared By:** Amna Rehman (2023-BS-AI-169)  

## Overview
This document records the final end-to-end verification and testing notes conducted during Week 8 to ensure system stability, correct API routing, and reliable vector retrieval prior to final project submission.

## Final Verification & Testing Observations

1. **Environment & Server Initialization:**
   - Successfully activated the virtual environment (`.\venv\Scripts\activate`) via PowerShell.
   - Initialized the FastAPI server using Uvicorn on port `8000` without any path or execution-policy errors.

2. **API Endpoint & Validation Testing:**
   - Sent valid query payloads to the `/query` endpoint; verified successful response codes (`200 OK`) and accurate context retrieval.
   - Tested malformed and short inputs (e.g., single characters); confirmed that Pydantic validation correctly intercepted them and returned `422 Unprocessable Entity`.

3. **Guardrail & Hallucination Prevention Check:**
   - Tested out-of-context and irrelevant queries against the similarity threshold (`0.35`).
   - Verified that the system successfully triggered the risk alert (*[Risk Guardrail Alert] Relevant information not found in context*) instead of hallucinating answers.

4. **Repository & Documentation Audit:**
   - Ensured all modular folders (`Week_1` to `Week_8`), the root `README.md`, and presentation slides are correctly organized and synchronized with GitHub.