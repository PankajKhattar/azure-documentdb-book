# Chapter 12 – AI and Vector Workloads with Azure DocumentDB

This repository contains the practical examples used in:

> Chapter 12 – AI and Vector Workloads with Azure DocumentDB

The examples demonstrate semantic retrieval, vector embeddings, recommendation systems, and Retrieval-Augmented Generation (RAG) concepts using Azure DocumentDB-compatible workflows.

---

# Repository Structure

```text
chapter-12-ai-workloads/
├── producer.js
├── embedding_receiver.py
├── semantic_search_example.py
├── recommendation_demo.py
├── rag_pipeline_example.md
└── README.md
```

---

# Objectives

The examples in this repository demonstrate:

- real-time embedding generation
- semantic search workflows
- vector similarity calculations
- recommendation systems
- Retrieval-Augmented Generation (RAG)

These examples are educational and intentionally simplified for clarity.

---

# Prerequisites

Install Python dependencies:

```bash
pip install pymongo
```

Install Node.js MongoDB driver:

```bash
npm install mongodb
```

---

# Environment Setup

Default connection string:

```python
mongodb://localhost:27017
```

Replace this with your Azure DocumentDB cluster endpoint if required.

---

# Example Files

---

# 1. producer.js

Simulates application-side document ingestion.

The script inserts documents into Azure DocumentDB.

Run:

```bash
node producer.js
```

---

# 2. embedding_receiver.py

Demonstrates a lightweight embedding generation pipeline using change streams.

When a new document is inserted:

- change stream event is triggered
- embedding is generated
- embedding is stored back into the document

Run:

```bash
python3 embedding_receiver.py
```

---

# 3. semantic_search_example.py

Demonstrates semantic similarity search using cosine similarity.

Topics covered:

- vector comparison
- semantic ranking
- embedding-based retrieval

Run:

```bash
python3 semantic_search_example.py
```

---

# 4. recommendation_demo.py

Demonstrates a lightweight recommendation engine using embedding similarity.

Topics covered:

- semantic recommendations
- vector similarity scoring
- ranking

Run:

```bash
python3 recommendation_demo.py
```

---

# 5. rag_pipeline_example.md

Contains conceptual examples and architecture notes related to Retrieval-Augmented Generation (RAG).

Topics covered:

- semantic retrieval
- prompt augmentation
- LLM integration
- contextual AI systems

---

# AI Workflow Overview

Typical AI workflow:

```text
Application
      ↓
Azure DocumentDB
      ↓
Change Stream
      ↓
Embedding Generator
      ↓
Vector Storage
      ↓
Semantic Retrieval
      ↓
LLM Inference
```

---

# Suggested Experiments

You can extend these examples by:

- integrating OpenAI embeddings
- adding Azure OpenAI
- implementing vector indexing
- integrating Redis caching
- adding ranking pipelines
- building chatbot applications

---

# Production Considerations

Production AI systems typically require:

- scalable embedding generation
- vector indexing optimization
- retrieval ranking
- prompt caching
- inference latency monitoring
- GPU-backed inference pipelines

The examples in this repository are simplified educational examples intended to explain AI retrieval concepts.

---

# Related Chapters

These examples complement:

- Chapter 8 – Query Engine and Indexing
- Chapter 9 – Change Streams
- Chapter 11 – Production-Grade Applications

---

# License

These examples are provided for educational and demonstration purposes.