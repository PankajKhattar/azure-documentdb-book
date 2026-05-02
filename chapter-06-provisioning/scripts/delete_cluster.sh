#!/bin/bash

CLUSTER_NAME=$1
RESOURCE_GROUP=$2

if [ -z "$CLUSTER_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
  echo "Usage: delete_cluster.sh <cluster-name> <resource-group>"
  exit 1
fi

echo "Deleting MongoDB vCore cluster..."

az resource delete \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --resource-type "Microsoft.DocumentDB/mongoClusters"

echo "Cluster deleted."