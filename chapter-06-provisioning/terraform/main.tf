provider "azurerm" {
  features {}
}

resource "azurerm_cosmosdb_account" "docdb" {
  name                = var.cluster_name
  location            = var.location
  resource_group_name = var.resource_group
  offer_type          = "Standard"
  kind                = "MongoDB"

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = var.location
    failover_priority = 0
  }
}