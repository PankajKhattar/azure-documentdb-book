# Scaling and Sharding Notes

Horizontal scalability is one of the most important characteristics of distributed databases.

Azure DocumentDB distributes data across shards to improve:

- scalability
- throughput
- fault isolation

---

# Example Shard Key

```javascript
{
  customerId: 1
}
```

---

# Good Shard Key Characteristics

A good shard key should:

- distribute data evenly
- avoid hotspots
- support query routing
- align with workload patterns

---

# Poor Shard Key Example

Using monotonically increasing values:

```javascript
{
  createdAt: 1
}
```

may result in uneven write distribution.

---

# Scatter-Gather Queries

Queries that do not include the shard key may execute across all shards.

Example:

```javascript
db.orders.find({
  amount: {
    $gt: 1000
  }
})
```

This may increase:

- latency
- network overhead
- CPU utilization

---

# Scaling Architecture

```text
Application Layer
        ↓
Router / Query Layer
        ↓
Shard 1
Shard 2
Shard 3
```

---

# Production Recommendations

- choose shard keys carefully
- monitor shard imbalance
- avoid cross-shard operations where possible
- test workload distribution under load