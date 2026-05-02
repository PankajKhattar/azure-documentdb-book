#!/bin/bash

CLUSTER_NAME=$1
RESOURCE_GROUP=$2
THROUGHPUT=$3

if [ -z "$THROUGHPUT" ]; then
  echo "Usage: scale_cluster.sh <cluster> <rg> <throughput>"
  exit 1
fi

echo "Scaling cluster to $THROUGHPUT RU/s..."

az cosmosdb mongodb database throughput update \
  --account-name $CLUSTER_NAME \
  --resource-group $RESOURCE_GROUP \
  --name mydb \
  --throughput $THROUGHPUT

echo "Scaling completed."