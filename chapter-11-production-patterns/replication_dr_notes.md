# Replication and Disaster Recovery Notes

Replication provides high availability and resilience in distributed systems.

Azure DocumentDB uses replica-based architectures to improve:

- availability
- failover handling
- durability

---

# Replication Concepts

Primary node:

- accepts writes
- replicates changes to replicas

Replica nodes:

- maintain synchronized copies
- serve failover operations

---

# Example Architecture

```text
Primary Node
     ↓
Replica 1
Replica 2
```

---

# Cross-Region Replication

Cross-region replication improves disaster recovery capabilities.

Benefits include:

- regional failover
- improved resilience
- geographic redundancy

---

# RPO and RTO

Recovery Point Objective (RPO):

- acceptable data loss window

Recovery Time Objective (RTO):

- acceptable recovery duration

---

# Graceful Failover

Graceful failovers occur during:

- maintenance
- planned upgrades

The system transitions traffic cleanly.

---

# Ungraceful Failover

Ungraceful failovers occur during:

- node crashes
- network failures
- infrastructure outages

Applications should implement retry handling and idempotency.

---

# Production Recommendations

- test failover regularly
- validate replication lag
- monitor replica health
- automate disaster recovery procedures