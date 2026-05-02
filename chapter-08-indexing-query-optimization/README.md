# Chapter 8: Indexing and Query Optimization

This repository demonstrates indexing strategies and query execution behavior for Azure DocunebtDB clusters.

---

## Concepts Covered

### 1. Path-Based Indexing

* Nested fields are indexed via extracted document paths
* Enables efficient querying on deeply nested structures

---

### 2. Single-Field Indexes

* Best for simple filters
* Limited for multi-dimensional queries

---

### 3. Composite Indexes

* Support filtering + sorting
* Field order is critical

---

### 4. Array Indexing (Multi-Key)

* Each element indexed separately
* Enables membership queries
* Increases index size

---

### 5. RUM-like Workloads

* Array containment queries
* Multi-term matching
* Simulates inverted index behavior

---

### 6. Query Planner Behavior

* Chooses between index scan vs sequential scan
* Depends on selectivity and cost

---

### 7. Scatter-Gather Impact

* Indexes do not prevent cross-shard queries
* Shard key must be included

---

## Key Takeaways

* Indexes must match **query patterns**, not schema
* Composite index order determines efficiency
* Array indexing increases write cost
* Planner may ignore indexes if not selective
* Shard key design is as important as indexing

---

## How to Run

```bash
pip install pymongo
python python/*.py
```

---

## Summary

Efficient query execution depends on:

* Correct index selection
* Understanding planner behavior
* Avoiding scatter-gather patterns

This chapter bridges theory with real execution patterns.
