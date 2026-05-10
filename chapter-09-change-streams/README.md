# Chapter 9 – Change Streams and Event-Driven Architectures

This repository contains the practical examples used in:

> Chapter 9 – Change Streams and Event-Driven Architectures in Azure DocumentDB

The examples demonstrate how applications can consume real-time database events using change streams.

---

# Repository Structure

```text
chapter-09-change-streams/
├── client.js
├── receiver.js
├── filtered_stream.js
├── checkpoint-store.js
└── README.md
```

---

# What Are Change Streams?

Change streams allow applications to listen to real-time changes occurring inside collections.

These changes may include:

- inserts
- updates
- deletes

Instead of polling the database repeatedly, applications can react immediately when data changes.

This enables event-driven architectures and real-time processing pipelines.

---

# Prerequisites

Install the MongoDB Node.js driver:

```bash
npm install mongodb
```

---

# Environment Setup

The examples use the following default connection string:

```javascript
mongodb://localhost:27017
```

Replace this with your Azure DocumentDB connection string if required.

---

# Example Files

---

# 1. client.js

Basic change stream listener.

This script continuously listens for changes in the `orders` collection and prints events to the console.

Run:

```bash
node client.js
```

---

# 2. receiver.js

Simulates an event-processing application.

This example demonstrates how downstream services can react to database events.

Example scenarios:

- order processing
- notifications
- analytics pipelines

Run:

```bash
node receiver.js
```

---

# 3. filtered_stream.js

Demonstrates filtered change streams using aggregation pipelines.

This example listens only for insert operations.

Run:

```bash
node filtered_stream.js
```

---

# 4. checkpoint-store.js

Implements lightweight resume token persistence.

Resume tokens allow applications to continue consuming events after failures or restarts.

This is important for production-grade event processing systems.

---

# Example Event

Example insert event:

```json
{
  "operationType": "insert",
  "fullDocument": {
    "_id": "order_101",
    "customerId": "C123",
    "amount": 1200
  }
}
```

---

# Suggested Experiments

You can extend these examples by:

- adding Kafka integration
- pushing events to Azure Event Hubs
- implementing retry handling
- scaling multiple consumers
- storing checkpoints in Redis or databases

---

# Architecture Overview

Typical event-driven flow:

```text
Application
    ↓
Azure DocumentDB
    ↓
Change Stream
    ↓
Event Consumer
    ↓
Downstream Systems
```

---

# Production Considerations

Production systems should additionally implement:

- retry handling
- durable checkpointing
- monitoring and alerting
- dead-letter queues
- consumer scaling


---

# License

These examples are provided for educational and demonstration purposes.