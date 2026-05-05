terraform {
  required_version = ">= 1.5"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_container_group" "api" {
  name                = "sales-prediction-api"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  ip_address_type     = "Public"
  dns_name_label      = "abc-analytics-api"

  container {
    name   = "sales-api"
    image  = "tiangolo/uvicorn-gunicorn-fastapi:python3.11"
    cpu    = "0.5"
    memory = "1.5"

    ports {
      port     = 8000
      protocol = "TCP"
    }

    environment_variables = {
      APP_ENV = "production"
    }
  }

  tags = {
    environment = var.entorno
    project     = "abc-analytics-migration"
    asignatura  = "20GIAR"
  }
}
