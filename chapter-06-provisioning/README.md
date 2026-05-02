# Chapter 6: Provisioning and Managing MongoDB vCore Clusters (Azure)

This repository provides **production-grade examples** for provisioning and managing **MongoDB vCore clusters** on Azure. It focuses on **cluster-based (vCore) architecture**, not RU-based deployments.

---

## Repository Structure

```
chapter-06-provisioning/
│
├── scripts/
│   ├── provision_cluster.sh     # (Optional/preview CLI)
│   ├── delete_cluster.sh        # Cleanup resources
│   ├── scale_cluster.sh         # Scale node count
│
├── arm/
│   ├── mongo-vcore.json         # ARM template for cluster provisioning
│
├── python/
│   ├── retry_example.py         # Retry with exponential backoff
│   ├── connection_manager.py    # Connection pooling & health checks
│
└── README.md
```

---

## 1. Provisioning MongoDB vCore Cluster (ARM Template)

### Why ARM?

MongoDB vCore cluster provisioning is **not fully available in standard Azure CLI**.
The most reliable method is using **ARM templates**.

---

### ARM Template

**File:** `arm/mongo-vcore.json`

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "clusterName": {
      "type": "string"
    },
    "location": {
      "type": "string",
      "defaultValue": "centralindia"
    },
    "administratorLogin": {
      "type": "string"
    },
    "administratorLoginPassword": {
      "type": "secureString"
    }
  },
  "resources": [
    {
      "type": "Microsoft.DocumentDB/mongoClusters",
      "apiVersion": "2023-03-15-preview",
      "name": "[parameters('clusterName')]",
      "location": "[parameters('location')]",
      "properties": {
        "administratorLogin": "[parameters('administratorLogin')]",
        "administratorLoginPassword": "[parameters('administratorLoginPassword')]",
        "nodeGroupSpecs": [
          {
            "kind": "Shard",
            "nodeCount": 3
          }
        ]
      }
    }
  ]
}
```

---

### Deploy the Template

```bash
az deployment group create \
  --resource-group my-rg \
  --template-file arm/mongo-vcore.json \
  --parameters clusterName=my-vcore-cluster \
               administratorLogin=adminuser \
               administratorLoginPassword=StrongPassword123!
```

---

## 2. Scaling Cluster (Conceptual Script)

```bash
# scripts/scale_cluster.sh

echo "Scaling MongoDB vCore cluster..."

# NOTE: Scaling is typically done via ARM update or Portal
# Placeholder for future CLI support

echo "Update nodeGroupSpecs in ARM template and redeploy."
```

---

## 3. Delete Cluster

```bash
az resource delete \
  --resource-group my-rg \
  --name my-vcore-cluster \
  --resource-type "Microsoft.DocumentDB/mongoClusters"
```

---

## 4. Application Resilience (Python)

### Install

```
pip install pymongo
```

---

### Retry Example

```python
from pymongo import MongoClient, errors
import time
import random

client = MongoClient("<connection-string>", serverSelectionTimeoutMS=5000)

def safe_query(max_retries=5):
    for attempt in range(max_retries):
        try:
            return client.db.users.find_one()

        except (errors.AutoReconnect, errors.NetworkTimeout):
            wait = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait)

    raise Exception("Failed after retries")
```

---

## 5. Connection Manager

```python
from pymongo import MongoClient

class MongoConnectionManager:
    def __init__(self, uri):
        self.client = MongoClient(
            uri,
            maxPoolSize=50,
            minPoolSize=5
        )

    def get_db(self, db_name):
        return self.client[db_name]

    def health_check(self):
        self.client.admin.command("ping")
        return True
```

---

## Architecture Overview

MongoDB vCore clusters follow a **true cluster model**:

* Primary + replica nodes
* Sharding support
* Dedicated compute (vCores)
* No RU abstraction

---

## Important Notes

* MongoDB vCore is exposed via **Microsoft.DocumentDB/mongoClusters**
* CLI support is **limited / preview**
* ARM / Portal are **recommended provisioning paths**

---

## Best Practices

* Use **ARM or Terraform** for repeatable deployments
* Implement **retry with exponential backoff**
* Monitor node utilization and scale proactively
* Secure credentials using **Azure Key Vault**
* Always design for **failover scenarios**

---

## Summary

This repository demonstrates:

* Real-world provisioning using ARM
* Cluster-based MongoDB architecture (vCore)
* Resilient application patterns
* Operational best practices

---

## Next Steps

* Add Terraform support for mongoClusters
* Integrate with Azure DevOps pipelines
* Add failover and chaos testing
* Benchmark performance vs RU-based systems

---

This chapter intentionally focuses on **cluster-based MongoDB (vCore)** to reflect modern, production-grade deployment patterns on Azure.
