# Observability Checklist

Production systems require strong observability practices.

This checklist helps validate operational readiness.

---

# Metrics

Monitor:

- query latency
- CPU utilization
- memory usage
- connection counts
- replication lag

---

# Logging

Ensure applications log:

- errors
- retries
- failovers
- slow queries

---

# Alerting

Create alerts for:

- high latency
- connection exhaustion
- node failures
- replication delays

---

# Query Diagnostics

Validate:

- index usage
- execution plans
- slow query behavior

---

# Failure Testing

Perform:

- failover testing
- load testing
- retry validation

---

# Capacity Planning

Review:

- storage growth
- throughput trends
- shard utilization

---

# Security Observability

Monitor:

- authentication failures
- unusual access patterns
- excessive permissions

---

# Recommended Tooling

Typical production environments integrate with:

- Azure Monitor
- Prometheus
- Grafana
- OpenTelemetry
- ELK Stack