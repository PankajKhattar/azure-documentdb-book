#!/bin/bash
set -e

CLUSTER_NAME=$1
RESOURCE_GROUP=$2
LOCATION=${3:-"centralindia"}

if [ -z "$CLUSTER_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
  echo "Usage: provision_cluster.sh <cluster-name> <resource-group> [location]"
  exit 1
fi

echo "Provisioning MongoDB vCore cluster via ARM..."

az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file ../arm/mongo-vcore.json \
  --parameters clusterName=$CLUSTER_NAME location=$LOCATION \
               administratorLogin=clusteradmin \
               administratorLoginPassword='StrongPassword123!'

echo "Provisioning complete."