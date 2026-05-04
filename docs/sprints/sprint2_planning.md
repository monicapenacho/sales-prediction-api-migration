# Sprint 2 — Planning y Ejecución

**Fechas:** 15/04/2026 – 28/04/2026  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Objetivo del Sprint:** Pipeline CI/CD activo en GitHub Actions con cobertura de tests garantizada.

---

## Sprint Goal

> "Al final del sprint, el pipeline CI/CD se ejecuta automáticamente en cada push, los tests pasan con cobertura ≥70% y la imagen Docker se sube a Azure Container Registry desde la rama principal."

---

## Sprint Backlog

| ID | Historia de Usuario | Estimación | Responsable | Estado |
|----|---------------------|-----------|-------------|--------|
| US-04 | Configurar GitHub Actions para CI/CD | 5 | Juan Manuel | ✅ Done |
| US-05 | Añadir cobertura de código ≥70% | 3 | Mónica | ✅ Done |
| US-08 | CD solo en rama principal | 3 | Juan Manuel | ✅ Done |
| US-09 | HEALTHCHECK en Dockerfile | 2 | Mónica | ✅ Done |

**Capacidad del sprint:** 13 puntos planificados → 13 completados ✅

---

## Tareas técnicas

### US-04 — GitHub Actions CI/CD
- [x] Crear `.github/workflows/ci.yml`
- [x] Job lint-and-test: checkout, setup-python, pip install, ruff, pytest
- [x] Job build-and-push: docker build, login ACR, tag, push
- [x] Verificar pipeline en verde en GitHub Actions

### US-05 — Cobertura
- [x] Añadir pytest-cov a requirements.txt
- [x] Configurar --cov-fail-under=70 en el pipeline
- [x] Verificar cobertura visible en el log del pipeline

### US-08 — CD en rama principal
- [x] Separar CI y CD en dos jobs independientes
- [x] Añadir condición if: github.ref == 'refs/heads/principal'
- [x] Verificar que CD no se dispara en otras ramas

### US-09 — HEALTHCHECK
- [x] Añadir HEALTHCHECK al Dockerfile
- [x] Añadir variables de entorno APP_VERSION y PORT

---

## Daily Standups (resumen)

| Día | Juan Manuel | Mónica | Impedimentos |
|-----|-------------|--------|--------------|
| 15/04 | Empezando ci.yml | Revisando Dockerfile | — |
| 18/04 | Pipeline CI configurado | HEALTHCHECK añadido | Error nombre archivos en español |
| 21/04 | Error corregido, pipeline verde | pytest-cov configurado | ModuleNotFoundError en tests |
| 24/04 | PYTHONPATH configurado, tests OK | Cobertura 75% verificada | — |
| 28/04 | CD separado en job independiente | Login ACR configurado | Secrets ACR pendientes |

---

## Sprint Review

**Demostrado:**
1. Pipeline CI/CD en verde en GitHub Actions
2. Cobertura de tests 75% visible en el log
3. Jobs CI y CD separados correctamente

**Pendiente para Sprint 3:** Configurar secrets ACR en GitHub para el CD completo.

---

## Métricas del Sprint

- **Velocidad:** 13 puntos
- **Cobertura de tests:** 75%
- **Tiempo de CI:** ~14 segundos
- **Bugs encontrados:** 2 (nombre archivos en español, ModuleNotFoundError)