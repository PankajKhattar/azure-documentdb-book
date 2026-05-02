#!/bin/bash

set -e

CLUSTER_NAME=${1:-"my-docdb-cluster"}
RESOURCE_GROUP=${2:-"my-rg"}
LOCATION=${3:-"centralindia"}

echo "Starting provisioning for Azure DocumentDB cluster..."
echo "Cluster: $CLUSTER_NAME"
echo "Resource Group: $RESOURCE_GROUP"
echo "Location: $LOCATION"

# Check if cluster already exists
EXISTS=$(az cosmosdb show \
  --name $CLUSTER_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "name" -o tsv 2>/dev/null || echo "")

if [ "$EXISTS" == "$CLUSTER_NAME" ]; then
  echo "Cluster already exists. Skipping provisioning."
  exit 0
fi

# Create cluster
az cosmosdb create \
  --name $CLUSTER_NAME \
  --resource-group $RESOURCE_GROUP \
  --locations regionName=$LOCATION \
  --kind MongoDB \
  --enable-free-tier false

echo "Provisioning completed successfully!"