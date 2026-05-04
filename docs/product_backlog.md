# Product Backlog — ABC Analytics Migration

**Asignatura:** Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos (20GIAR)  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Proyecto:** Proyecto 3 — Migración Cloud  

---

## Épicas

| # | Épica | Descripción |
|---|-------|-------------|
| E1 | API | Desarrollo de la API de predicción de ventas |
| E2 | Contenedores | Containerización con Docker |
| E3 | CI/CD | Pipeline automatizado de integración y despliegue |
| E4 | IaC | Infraestructura Azure como código con Terraform |
| E5 | Metodología | Gestión ágil del proyecto |

---

## Backlog Priorizado (MoSCoW)

### Must Have (obligatorio para MVP)

| ID | Épica | Historia de Usuario | Criterios de Aceptación | Puntos |
|----|-------|---------------------|------------------------|--------|
| US-01 | E1 | Como desarrollador, quiero crear la API FastAPI de predicción de ventas, para simular el servicio on-premise | API arranca con uvicorn; endpoints /, /health y /predict responden correctamente; tests pasan | 5 |
| US-02 | E2 | Como desarrollador, quiero dockerizar la aplicación, para prepararla para el despliegue en cloud | docker build ejecuta sin errores; docker run arranca la API en puerto 8000 | 3 |
| US-03 | E1 | Como desarrollador, quiero escribir tests unitarios con pytest, para garantizar la calidad del código | Tests cubren los 3 endpoints; cobertura ≥ 70%; pytest pasa sin errores | 5 |
| US-04 | E3 | Como DevOps, quiero configurar GitHub Actions para CI/CD, para automatizar tests en cada push | Pipeline se dispara en cada push; lint y tests se ejecutan automáticamente | 5 |
| US-05 | E3 | Como DevOps, quiero añadir cobertura de código ≥70%, para garantizar calidad mínima | pytest --cov-fail-under=70 pasa en verde; cobertura visible en el log del pipeline | 3 |
| US-06 | E4 | Como DevOps, quiero crear la infraestructura en Azure con Terraform, para desplegar de forma reproducible | terraform plan sin errores; terraform apply crea Resource Group y Container Instance en Azure | 8 |
| US-07 | E4 | Como DevOps, quiero desplegar la aplicación en Azure Container Instances, para tenerla en producción | Contenedor en estado Running en Azure portal; API accesible por IP pública | 8 |

### Should Have (importante, no bloqueante)

| ID | Épica | Historia de Usuario | Criterios de Aceptación | Puntos |
|----|-------|---------------------|------------------------|--------|
| US-08 | E3 | Como DevOps, quiero que el CD solo se ejecute en la rama principal, para evitar despliegues accidentales | Job build-and-push solo se dispara en rama principal y solo si CI pasa | 3 |
| US-09 | E2 | Como DevOps, quiero añadir HEALTHCHECK al Dockerfile, para que Azure detecte si el contenedor está sano | HEALTHCHECK definido en Dockerfile; Azure marca el contenedor como healthy | 2 |

### Could Have (deseable)

| ID | Épica | Historia de Usuario | Criterios de Aceptación | Puntos |
|----|-------|---------------------|------------------------|--------|
| US-10 | E4 | Como DevOps, quiero configurar Azure Monitor para observabilidad, para detectar problemas en producción | Logs de la API visibles en Azure Monitor; alertas configuradas | 5 |
| US-11 | E1 | Como desarrollador, quiero añadir autenticación a la API, para proteger el acceso en producción | Endpoint /predict requiere token de autenticación | 8 |

---

## Velocidad del equipo

| Sprint | Puntos planificados | Puntos completados | % completado |
|--------|--------------------|--------------------|--------------|
| Sprint 1 | 13 | 13 | 100% |
| Sprint 2 | 10 | 10 | 100% |
| Sprint 3 | 8 | 6 | 75% |
| **Total** | **31** | **29** | **94%** |