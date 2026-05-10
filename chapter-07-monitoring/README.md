# Chapter 7 – Monitoring, Observability, and Diagnostics in Azure DocumentDB

This repository contains the practical examples and scripts used in **Chapter 7** of the book:

> **Azure DocumentDB for MongoDB: Architecture, Operations, and Performance**

The examples in this chapter focus on operational visibility, query diagnostics, performance monitoring, and troubleshooting techniques for Azure DocumentDB environments.

---

# Repository Structure

```text
chapter-07-monitoring/
├── metrics_collector.py
├── slow_query_monitor.js
├── replication_check.py
├── connection_monitor.py
├── latency_test.py
└── README.md
```

---

# Objectives of This Chapter

The scripts included in this repository demonstrate:

- collecting operational metrics
- measuring query latency
- diagnosing slow queries
- monitoring database connections
- validating workload performance
- understanding observability workflows

These examples are intentionally lightweight so they can be easily understood and extended.

---

# Prerequisites

## Python Requirements

Install Python dependencies:

```bash
pip install pymongo
```

---

## Node.js Requirements

Install the MongoDB Node.js driver:

```bash
npm install mongodb
```

---

# Environment Setup

These examples assume a MongoDB-compatible endpoint such as:

- Azure DocumentDB
- Azure Cosmos DB for MongoDB
- MongoDB Community Edition
- DocumentDB OSS local environment

Default connection string used in examples:

```python
mongodb://localhost:27017
```

Replace this value with your Azure DocumentDB connection string if required.

---

# Example Scripts

---

# 1. metrics_collector.py

This script retrieves basic operational statistics from the database.

It demonstrates how monitoring systems can collect:

- collection count
- document count
- storage usage
- index statistics

---

## Example Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["shop"]

stats = db.command("dbStats")

print("Collections:", stats["collections"])
print("Objects:", stats["objects"])
print("Storage Size:", stats["storageSize"])
print("Indexes:", stats["indexes"])
```

---

## Run

```bash
python3 metrics_collector.py
```

---

# 2. slow_query_monitor.js

This script measures query latency and detects slow queries.

The example demonstrates how applications can implement lightweight performance diagnostics.

---

## Example Code

```javascript
const { MongoClient } = require("mongodb");

async function run() {
  const client = new MongoClient("mongodb://localhost:27017");

  await client.connect();

  const db = client.db("shop");

  const start = Date.now();

  await db.collection("orders")
    .find({ status: "completed" })
    .toArray();

  const latency = Date.now() - start;

  console.log("Query latency:", latency, "ms");

  if (latency > 100) {
    console.log("WARNING: Slow query detected");
  }

  await client.close();
}

run();
```

---

## Run

```bash
node slow_query_monitor.js
```

---

# 3. replication_check.py

This script retrieves server-level diagnostic information.

It demonstrates how operational tooling can inspect server health and runtime statistics.

---

## Example Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

status = client.admin.command("serverStatus")

print("Connections:", status["connections"])
print("Uptime:", status["uptime"])
```

---

## Run

```bash
python3 replication_check.py
```

---

# 4. connection_monitor.py

This example demonstrates connection pooling configuration.

Improper connection handling is one of the most common causes of production instability in distributed systems.

---

## Example Code

```python
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017",
    maxPoolSize=50
)

print(client)
```

---

## Run

```bash
python3 connection_monitor.py
```

---

# 5. latency_test.py

This script performs repeated database queries to simulate lightweight benchmarking workloads.

Useful for:

- comparing query performance
- validating indexing improvements
- observing latency behavior

---

## Example Code

```python
import time
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

collection = client.db.orders

start = time.time()

for _ in range(1000):
    collection.find_one({"customerId": "C123"})

print("Elapsed:", time.time() - start)
```

---

## Run

```bash
python3 latency_test.py
```

---

# Monitoring Concepts Covered

The examples in this repository align with the following concepts discussed in Chapter 7:

| Concept | Example |
|---|---|
| Metrics Collection | metrics_collector.py |
| Query Latency Monitoring | slow_query_monitor.js |
| Server Diagnostics | replication_check.py |
| Connection Management | connection_monitor.py |
| Benchmarking | latency_test.py |

---

# Suggested Experiments

You can extend these examples by:

- testing indexed vs non-indexed queries
- increasing concurrency
- introducing artificial workload spikes
- measuring latency under load
- integrating with external monitoring tools

---

# Production Considerations

Production-grade monitoring systems typically integrate with:

- Azure Monitor
- Prometheus
- Grafana
- OpenTelemetry
- ELK Stack

The scripts in this repository are educational examples designed to explain the core principles behind observability and diagnostics.

---

# License

These examples are provided for educational and demonstration purposes.