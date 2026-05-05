# Memoria del Proyecto: ABC Analytics — Migración Cloud

**Asignatura:** Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos (20GIAR)  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Proyecto:** Proyecto 3 — Migración Cloud  
**Repositorio:** https://github.com/jmcampos-sec/sales-prediction-api-migration  
**Fecha:** 06/05/2026  

---

## 1. Resumen Ejecutivo

ABC Analytics opera una API de predicción de ventas en servidores on-premise con limitaciones críticas: falta de escalabilidad, ausencia de automatización en despliegues y elevados costes de mantenimiento físico.

**El problema:** La infraestructura on-premise no permite escalar en momentos de alta demanda, los despliegues son manuales y propensos a errores, y el coste de mantenimiento de servidores físicos es elevado.

**Nuestra solución:** Migración completa a Azure aplicando las estrategias de las 6R vistas en clase (Rehosting + modernización):
1. Containerización de la API con Docker
2. Pipeline CI/CD automatizado con GitHub Actions
3. Infraestructura como Código con Terraform
4. Despliegue en Azure Container Instances (Spain Central)

**Resultado obtenido:**
- API REST funcional con 3 endpoints
- Pipeline CI/CD en verde con cobertura de tests del 75%
- Infraestructura Azure desplegada con Terraform en 68 segundos
- 2 recursos creados: Resource Group + Container Instance

---

## 2. Descripción del Problema y Caso de Negocio

### 2.1 Contexto

ABC Analytics es una empresa de análisis de datos que dispone de una API de predicción de ventas desplegada en servidores on-premise. Esta infraestructura presenta los siguientes problemas:

- **Escalabilidad:** Los servidores físicos no pueden escalar automáticamente ante picos de demanda
- **Disponibilidad:** Sin redundancia geográfica ni failover automático
- **Costes:** El mantenimiento de hardware supone un coste fijo elevado independientemente del uso
- **Despliegues:** Proceso manual, lento y propenso a errores humanos

### 2.2 Valor de negocio

La migración a Azure permite:
- Reducir el tiempo de despliegue de horas a minutos
- Escalar recursos bajo demanda según el tráfico
- Eliminar costes de mantenimiento de hardware físico
- Garantizar reproducibilidad total del entorno con Terraform

### 2.3 Estrategia de migración — Las 6R

Siguiendo las 6R de migración cloud vistas en clase, se ha optado por:

| Estrategia | Descripción | Aplicación en ABC Analytics |
|-----------|-------------|----------------------------|
| Rehost | Lift & Shift | Contenedor Docker en Azure Container Instances |
| Replatform | Modernización parcial | FastAPI + uvicorn en lugar de servidor legacy |

---

## 3. Arquitectura de la Solución

### 3.1 Diagrama de arquitectura
DESARROLLADOR
│  git push
▼
GITHUB REPOSITORY
│
├──(push cualquier rama)──► CI Job (lint + tests + cobertura ≥70%)
│
└──(push a principal)──────► CD Job (build Docker → push ACR → deploy)
AZURE (Spain Central)
├── Azure Container Registry → Imágenes Docker
├── Azure Container Instances → API en producción (puerto 8000)
└── Resource Group rg-abc-analytics → Contenedor de recursos

### 3.2 Justificación de tecnologías

| Componente | Tecnología | Por qué esta y no otra |
|------------|-----------|------------------------|
| Lenguaje | Python 3.11 | Estándar en Data Science; ecosistema maduro |
| API | FastAPI | Más rápido que Flask; documentación automática con Swagger |
| Contenedores | Docker | Reproducibilidad garantizada; estándar de la industria |
| CI/CD | GitHub Actions | Integrado con el repositorio; visto en clase |
| Cloud | Azure | Trabajado durante el curso; cuenta de estudiante disponible |
| IaC | Terraform | Multi-cloud; HCL legible; visto en clase |
| Lint | Ruff | Más rápido que flake8; moderno |

**¿Por qué Azure y no AWS?**
AWS Educate no proporciona acceso a servicios reales de infraestructura necesarios para ejecutar Terraform. Azure Students ofrece 100$ de crédito con el correo universitario, sin tarjeta de crédito, y es la plataforma trabajada durante el curso.

---

## 4. Implementación

### 4.1 Estructura del proyecto
sales-prediction-api-migration/
├── app/
│   ├── init.py
│   ├── main.py          # API FastAPI
│   └── models.py        # Modelos Pydantic
├── tests/
│   ├── init.py
│   └── test_main.py     # Tests unitarios
├── terraform/
│   ├── main.tf          # Recursos Azure
│   ├── variables.tf     # Variables
│   └── outputs.tf       # Outputs
├── .github/workflows/
│   └── ci.yml           # Pipeline CI/CD
├── Dockerfile           # Imagen Docker
├── requirements.txt     # Dependencias
└── docs/                # Documentación

### 4.2 API FastAPI — Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Confirma que la API está funcionando |
| `/health` | GET | Health check para monitorización |
| `/predict` | POST | Predicción de ventas (producto, ventas base, mes) |

### 4.3 Pipeline CI/CD

El pipeline tiene dos jobs separados:

**Job 1 — lint-and-test (todas las ramas):**
- Lint con ruff
- Tests con pytest
- Cobertura ≥ 70%

**Job 2 — build-and-push (solo rama principal):**
- Solo se ejecuta si el Job 1 pasa
- Build de imagen Docker
- Push a Azure Container Registry

### 4.4 Infraestructura como Código

Terraform aprovisiona en Azure:
- `azurerm_resource_group` — Grupo de recursos en Spain Central
- `azurerm_container_group` — Contenedor con la API en puerto 8000
terraform apply completado en 68 segundos
2 resources added, 0 changed, 0 destroyed

### 4.5 Dificultades encontradas

| Dificultad | Causa | Solución |
|-----------|-------|----------|
| Pipeline CI fallaba | Nombre archivos en español | Corregir rutas en ci.yml |
| ModuleNotFoundError | Faltaban __init__.py | Añadir archivos y PYTHONPATH |
| Terraform sin permisos | Cuenta estudiante limitada | skip_provider_registration = true |
| AWS Educate no funciona | Solo da acceso a cursos | Migrar a Azure Students |

---

## 5. Metodología Ágil

### 5.1 Framework SCRUM

Sprints de 2 semanas con las siguientes ceremonias:
- **Sprint Planning:** inicio de cada sprint
- **Sprint Review:** final de cada sprint con demo
- **Sprint Retrospective:** lecciones aprendidas

### 5.2 Tablero GitHub Projects

Columnas: `Reserva → Listo → En curso → En revisión → Hecho`

### 5.3 Velocidad del equipo

| Sprint | Puntos planificados | Puntos completados | % completado |
|--------|--------------------|--------------------|--------------|
| Sprint 1 | 13 | 13 | 100% |
| Sprint 2 | 10 | 10 | 100% |
| Sprint 3 | 8 | 6 | 75% |
| **Total** | **31** | **29** | **94%** |

---

## 6. Resultados y Métricas

| Métrica | Objetivo | Resultado |
|---------|----------|-----------|
| Cobertura de tests | ≥ 70% | 75% ✅ |
| Pipeline CI/CD | Verde en cada push | ✅ Funcionando |
| Infraestructura IaC | Reproducible | ✅ terraform apply |
| Despliegue Azure | Contenedor en ejecución | ✅ Spain Central |

### 6.2 Coste estimado (Azure Students)

| Recurso | Coste estimado |
|---------|---------------|
| Azure Container Instances (0.5 vCPU, 1.5 GB) | ~3.50€/mes |
| Azure Container Registry (Basic) | ~5.00€/mes |
| **Total** | **~8.50€/mes** |

---

## 7. Conclusiones

1. **La containerización con Docker garantiza reproducibilidad:** el mismo contenedor funciona en local y en Azure sin cambios.
2. **Terraform es indispensable para la reproducibilidad de la infraestructura:** recrear el entorno completo tarda 68 segundos.
3. **El pipeline CI/CD detecta errores automáticamente:** varios bugs fueron detectados por los tests antes de llegar a producción.
4. **La metodología Scrum permitió organizar el trabajo de forma iterativa** con objetivos claros por sprint.

### 7.1 Próximos pasos

- Subir imagen Docker personalizada a Azure Container Registry
- Configurar Azure Monitor para observabilidad
- Implementar estrategia de despliegue Canary
- Añadir autenticación con Azure Active Directory

---

## 8. Bibliografía

- Kim, G., Humble, J., Debois, P. y Willis, J. (2021). *The DevOps Handbook*. IT Revolution Press.
- Documentación oficial FastAPI: https://fastapi.tiangolo.com/
- Documentación oficial Terraform Azure Provider: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- Documentación oficial Azure Container Instances: https://docs.microsoft.com/azure/container-instances/
- Documentación oficial GitHub Actions: https://docs.github.com/actions