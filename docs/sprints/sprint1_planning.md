# Sprint 1 — Planning y Ejecución

**Fechas:** 1/04/2026 – 14/04/2026  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Objetivo del Sprint:** Tener la API de predicción de ventas funcional y dockerizada con tests unitarios.

---

## Sprint Goal

> "Al final del sprint, disponemos de una API FastAPI funcional con tests unitarios y containerizada con Docker, lista para ser desplegada en cloud."

---

## Sprint Backlog

| ID | Historia de Usuario | Estimación | Responsable | Estado |
|----|---------------------|-----------|-------------|--------|
| US-01 | Crear API FastAPI de predicción de ventas | 5 | Juan Manuel | ✅ Done |
| US-02 | Dockerizar la aplicación | 3 | Mónica | ✅ Done |
| US-03 | Escribir tests unitarios con pytest | 5 | Juan Manuel | ✅ Done |

**Capacidad del sprint:** 13 puntos planificados → 13 completados ✅

---

## Tareas técnicas

### US-01 — API FastAPI
- [x] Crear `app/main.py` con endpoints /, /health y /predict
- [x] Crear `app/models.py` con modelos Pydantic
- [x] Crear `app/__init__.py`
- [x] Verificar que la API arranca con uvicorn

### US-02 — Dockerización
- [x] Crear `Dockerfile` con python:3.11-slim
- [x] Añadir HEALTHCHECK al Dockerfile
- [x] Verificar docker build sin errores
- [x] Verificar docker run en puerto 8000

### US-03 — Tests
- [x] Crear `tests/test_main.py` con tests de los 3 endpoints
- [x] Crear `tests/__init__.py`
- [x] Verificar cobertura ≥ 70%
- [x] pytest pasa sin errores

---

## Daily Standups (resumen)

| Día | Juan Manuel | Mónica | Impedimentos |
|-----|-------------|--------|--------------|
| 01/04 | Setup del repositorio GitHub | Setup del entorno Python | — |
| 03/04 | Estructura de carpetas creada | Empezando Dockerfile | — |
| 07/04 | API FastAPI con endpoints básicos | Docker build funcionando | — |
| 10/04 | Modelos Pydantic completados | Docker run OK en puerto 8000 | — |
| 14/04 | Tests unitarios completos, cobertura 75% | HEALTHCHECK añadido | — |

---

## Sprint Review

**Demostrado:**
1. API arrancando con uvicorn localmente
2. docker build y docker run funcionando
3. pytest con 75% de cobertura

**No completado:** Todo completado en este sprint.

---

## Métricas del Sprint

- **Velocidad:** 13 puntos
- **Cobertura de tests:** 75%
- **Bugs encontrados:** 1 (ModuleNotFoundError — resuelto con __init__.py y PYTHONPATH)