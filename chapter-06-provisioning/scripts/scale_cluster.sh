#!/bin/bash

CLUSTER_NAME=$1
RESOURCE_GROUP=$2
NODE_COUNT=$3

if [ -z "$NODE_COUNT" ]; then
  echo "Usage: scale_cluster.sh <cluster> <rg> <node-count>"
  exit 1
fi

echo "Scaling cluster via ARM redeployment..."

az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file ../arm/mongo-vcore.json \
  --parameters clusterName=$CLUSTER_NAME \
               nodeCount=$NODE_COUNT \
               administratorLogin=clusteradmin \
               administratorLoginPassword='StrongPassword123!'

echo "Scaling complete."