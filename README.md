# ABC Analytics — Migración Cloud: API de Predicción de Ventas

> **Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos (20GIAR)**

**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Proyecto elegido:** Proyecto 3 — Migración Cloud  
**Repositorio:** https://github.com/jmcampos-sec/sales-prediction-api-migration

---

## Descripción

Migración completa de una API de predicción de ventas desde infraestructura on-premise a Microsoft Azure,
aplicando prácticas DevOps modernas: containerización con Docker, pipeline CI/CD con GitHub Actions e
Infraestructura como Código con Terraform.

**Caso de negocio:** ABC Analytics opera una API de predicción de ventas en servidores físicos con
limitaciones críticas de escalabilidad y costes elevados de mantenimiento. La migración a Azure
reduce el tiempo de despliegue de horas a minutos y garantiza reproducibilidad total del entorno.

---

## Arquitectura
DESARROLLADOR
│  git push
▼
GITHUB REPOSITORY
│
├─(push cualquier rama)──► Job: lint-and-test
│                               ruff + pytest
│                               cobertura ≥ 70%
│
└─(push a principal)─────► Job: build-and-push
Build Docker image
Push a Azure Container Registry
AZURE (Spain Central)
├── Resource Group: rg-abc-analytics
└── Container Instance: sales-prediction-api
/predict  /health  /
Puerto 8000 — IP Pública

---

## Requisitos previos

- Python 3.11+
- Docker + Docker Compose
- Terraform 1.5+
- Azure CLI configurado (`az login`)
- Cuenta Azure Students (100$ crédito gratuito)

---

## Inicio rápido (local)

```bash
# 1. Clonar el repositorio
git clone https://github.com/jmcampos-sec/sales-prediction-api-migration
cd sales-prediction-api-migration

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Ejecutar tests
pytest tests/ --cov=app --cov-report=term-missing

# 4. Levantar la API en Docker
docker-compose up --build

# 5. Probar la API
curl http://localhost:8000/health

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"product": "ProductoA", "base_sales": 1000.0, "month": 5}'
```

---

## Documentación Swagger

Con la API en marcha, accede a la documentación automática en:
http://localhost:8000/docs

---

## Resultados y Métricas

| Métrica | Objetivo | Resultado |
|---------|----------|-----------|
| Cobertura de tests | ≥ 70% | 75% ✅ |
| Pipeline CI/CD | Verde en cada push | ✅ |
| Terraform apply | Reproducible | 68 seg ✅ |
| Contenedor Azure | Running | ✅ Spain Central |
| Coste infraestructura | — | ~8.50€/mes |

---

## Estructura del repositorio
sales-prediction-api-migration/
├── .github/workflows/
│   └── ci.yml                  # Pipeline CI/CD (lint + tests + build + push)
├── app/
│   ├── init.py
│   ├── main.py                 # API FastAPI: /, /health, /predict
│   └── models.py               # Pydantic schemas
├── tests/
│   ├── init.py
│   └── test_main.py            # Tests unitarios de todos los endpoints
├── terraform/
│   ├── main.tf                 # Recursos Azure (Resource Group + Container Instance)
│   ├── variables.tf            # Variables de configuración
│   └── outputs.tf              # Outputs (URL pública, resource group, location)
├── docs/
│   ├── memoria_proyecto.md     # Memoria completa del proyecto
│   ├── product_backlog.md      # Product Backlog con User Stories
│   └── sprints/
│       ├── sprint1_planning.md
│       ├── sprint2_planning.md
│       ├── sprint3_planning.md
│       └── retrospectiva.md
├── presentacion/
│   └── guia_presentacion.md    # Guía de presentación con timings
├── Dockerfile                  # Imagen Docker de la API
├── docker-compose.yml          # Para desarrollo local
└── requirements.txt            # Dependencias Python

---

## CI/CD

| Job | Trigger | Qué hace |
|-----|---------|----------|
| `lint-and-test` | Push a cualquier rama | Lint con ruff + tests con pytest + cobertura ≥70% |
| `build-and-push` | Push a rama principal | Build Docker + push a Azure Container Registry |

El job `build-and-push` solo se ejecuta si `lint-and-test` pasa correctamente.

---

## Infraestructura Azure (Terraform)

Recursos desplegados con `terraform apply`:

- **Resource Group** `rg-abc-analytics` — contenedor de recursos en Spain Central
- **Container Instance** `sales-prediction-api` — API en producción con IP pública

```bash
cd terraform/
terraform init
terraform plan
terraform apply
```

URL de la API desplegada:
http://abc-analytics-api.spaincentral.azurecontainer.io:8000

---

## Endpoints de la API

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Confirma que la API está funcionando |
| `/health` | GET | Health check para monitorización del contenedor |
| `/predict` | POST | Predicción de ventas (product, base_sales, month) |

**Ejemplo de request:**
```json
{
  "product": "ProductoA",
  "base_sales": 1000.0,
  "month": 5
}
```

**Ejemplo de response:**
```json
{
  "product": "ProductoA",
  "predicted_sales": 1187.43,
  "confidence": 0.87
}
```

---

## Metodología Ágil

Proyecto gestionado con **Scrum** y sprints de 2 semanas:

| Sprint | Objetivo | Estado |
|--------|----------|--------|
| Sprint 1 | API FastAPI + Docker + Tests | ✅ Completado |
| Sprint 2 | CI/CD + Cobertura ≥70% | ✅ Completado |
| Sprint 3 | Terraform + Azure | 🔄 En curso |

Tablero Kanban disponible en **GitHub Projects**.

---

## Decisión sobre plataforma cloud

El enunciado indica AWS, pero se ha utilizado **Azure** por las siguientes razones:

1. Azure fue la plataforma trabajada durante el curso
2. AWS Educate no proporciona acceso a servicios reales de infraestructura (solo cursos)
3. Azure Students ofrece 100$ de crédito con el correo universitario, sin tarjeta de crédito

Los conceptos aplicados (Terraform, Docker, CI/CD) son equivalentes en ambas plataformas.

---

## Tecnologías

| Componente | Tecnología | Versión |
|------------|-----------|---------|
| API | FastAPI | 0.110.0 |
| Runtime | Python | 3.11 |
| Contenedor | Docker | — |
| CI/CD | GitHub Actions | — |
| IaC | Terraform | ≥ 1.5 |
| Cloud | Microsoft Azure | — |
| Tests | pytest + pytest-cov | 8.1.1 |
| Lint | ruff | 0.4.4 |
