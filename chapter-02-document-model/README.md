# Chapter 2 – Document Model & APIs

This chapter introduces the **document data model** used by **Azure DocumentDB** and demonstrates how documents are created and stored using a MongoDB-compatible API.

The examples here focus on:
- BSON documents
- Nested fields
- Schema flexibility
- Basic insert operations


## Prerequisites

- DocumentDB OSS running locally
- Node.js 18+ or Python 3.9+

DocumentDB OSS must be reachable at:
mongodb://localhost:27017

## Folder Structure
```bash
chapter-02-document-model/
├── nodejs/
│ └── insert-basic.js
├── python/
│ └── insert-basic.py
├── data/
│ └── sample-users.json
└── README.md
```

## Running the Examples

### Node.js
```bash
cd nodejs
node insert-basic.js
```

### Python
```bash
cd python
python insert-basic.py
