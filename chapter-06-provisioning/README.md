# Chapter 6: Provisioning and Managing Azure DocumentDB Clusters

This repository contains production-grade examples demonstrating how to provision, manage, and interact with Azure DocumentDB (MongoDB API) clusters. The focus is on real-world practices including automation, resilience, and infrastructure-as-code.

---

## Repository Structure

```
chapter-06-provisioning/
│
├── scripts/
│   ├── provision_cluster.sh     # Create cluster (idempotent)
│   ├── delete_cluster.sh        # Cleanup resources
│   ├── scale_cluster.sh         # Adjust throughput
│
├── python/
│   ├── retry_example.py         # Retry with exponential backoff
│   ├── connection_manager.py    # Connection pooling & health checks
│
├── terraform/
│   ├── main.tf                  # Cosmos DB provisioning
│   ├── variables.tf             # Configurable inputs
│
└── README.md
```

---

## 1. Provisioning a Cluster (Azure CLI)

### Prerequisites

* Azure CLI installed
* Logged in using:

  ```
  az login
  ```

### Run Script

```
chmod +x scripts/provision_cluster.sh

./scripts/provision_cluster.sh <cluster-name> <resource-group> <location>
```

### Example

```
./scripts/provision_cluster.sh my-docdb my-rg centralindia
```

### Key Features

* Idempotent (won’t recreate existing cluster)
* Parameterized inputs
* Error-safe execution

---

## 2. Scaling Throughput

```
chmod +x scripts/scale_cluster.sh

./scripts/scale_cluster.sh <cluster-name> <resource-group> <throughput>
```

### Example

```
./scripts/scale_cluster.sh my-docdb my-rg 1000
```

---

## 3. Deleting the Cluster

```
chmod +x scripts/delete_cluster.sh

./scripts/delete_cluster.sh my-docdb my-rg
```

---

## 4. Resilient Application Layer (Python)

### Install Dependencies

```
pip install pymongo
```

### Retry Example

```
python python/retry_example.py
```

### What It Demonstrates

* Handling transient failures
* Exponential backoff
* Retry-safe operations

---

## 5. Connection Management

```
from connection_manager import MongoConnectionManager

manager = MongoConnectionManager("<connection-string>")
db = manager.get_db("test")

if manager.health_check():
    print("Connection is healthy")
```

### Features

* Connection pooling
* Health checks
* Configurable timeouts

---

## 6. Infrastructure as Code (Terraform)

### Initialize

```
cd terraform
terraform init
```

### Plan

```
terraform plan \
  -var="cluster_name=my-docdb" \
  -var="resource_group=my-rg"
```

### Apply

```
terraform apply \
  -var="cluster_name=my-docdb" \
  -var="resource_group=my-rg"
```

---

## Architecture Overview

This chapter demonstrates a layered approach:

1. **Provisioning Layer**

   * Azure CLI scripts
   * Terraform (declarative)

2. **Operations Layer**

   * Scaling scripts
   * Resource lifecycle management

3. **Application Layer**

   * Retry logic
   * Connection pooling
   * Health monitoring

---

## Best Practices

* Always use **retry with backoff** for distributed systems
* Prefer **Infrastructure-as-Code (Terraform)** over manual provisioning
* Monitor **throughput (RU/s)** and scale proactively
* Use **connection pooling** to reduce latency
* Design for **failure, not success**

---

## Next Steps

To extend this setup:

* Integrate with Azure DevOps pipelines
* Add automated failover testing
* Implement observability (metrics + logging)
* Introduce chaos testing for resilience validation

---

## Summary

This repository bridges the gap between:

* Simple provisioning examples
  and
* Production-ready cluster management

It equips you with the tools and patterns needed to operate Azure DocumentDB clusters reliably at scale.
