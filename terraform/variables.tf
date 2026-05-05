variable "resource_group_name" {
  description = "Nombre del grupo de recursos en Azure"
  type        = string
  default     = "rg-abc-analytics"
}

variable "location" {
  description = "Región de Azure para el despliegue"
  type        = string
  default     = "Spain Central"
}

variable "api_image" {
  description = "Imagen Docker de la API"
  type        = string
  default     = "tiangolo/uvicorn-gunicorn-fastapi:python3.11"
}

variable "entorno" {
  description = "Entorno: dev | staging | prod"
  type        = string
  default     = "dev"
}