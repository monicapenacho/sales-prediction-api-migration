# Sprint 3 — Planning y Ejecución

**Fechas:** 29/04/2026 – 06/05/2026  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Objetivo del Sprint:** Infraestructura Azure desplegada con Terraform y entregables finales listos.

---

## Sprint Goal

> "Al final del sprint, la infraestructura está desplegada en Azure con Terraform, el contenedor está en ejecución y los entregables del portafolio están listos."

---

## Sprint Backlog

| ID | Historia de Usuario | Estimación | Responsable | Estado |
|----|---------------------|-----------|-------------|--------|
| US-06 | Crear infraestructura en Azure con Terraform | 8 | Juan Manuel | ✅ Done |
| US-07 | Desplegar aplicación en Azure Container Instances | 8 | Mónica | 🔄 En curso |
| — | Documentación (memoria, backlog, sprints) | — | Ambos | ✅ Done |
| — | Preparación presentación/vídeo | — | Ambos | 🔄 En curso |

**Capacidad del sprint:** 16 puntos planificados → 12 completados (US-07 parcial)

---

## Tareas técnicas

### US-06 — Terraform
- [x] Crear `terraform/main.tf` con Resource Group y Container Instance
- [x] Crear `terraform/variables.tf` con variables de configuración
- [x] Crear `terraform/outputs.tf` con URL de la API
- [x] terraform init ejecutado sin errores
- [x] terraform plan: 2 recursos a crear
- [x] terraform apply: 2 recursos creados en 68 segundos

### US-07 — Despliegue Azure
- [x] Contenedor en estado Running en Azure portal
- [x] Resource Group rg-abc-analytics visible en Azure
- [ ] API respondiendo por URL pública (imagen personalizada pendiente)
- [ ] Azure Container Registry configurado con imagen propia

### Documentación
- [x] docs/memoria_proyecto.md
- [x] docs/product_backlog.md
- [x] docs/sprints/sprint1_planning.md
- [x] docs/sprints/sprint2_planning.md
- [x] docs/sprints/sprint3_planning.md
- [x] docs/sprints/retrospectiva.md
- [x] README.md completo

---

## Daily Standups (resumen)

| Día | Juan Manuel | Mónica | Impedimentos |
|-----|-------------|--------|--------------|
| 29/04 | Creando archivos Terraform | Revisando documentación | — |
| 01/05 | terraform init OK | Empezando memoria | — |
| 03/05 | terraform plan OK | Product backlog completado | Terraform sin permisos AWS |
| 04/05 | Migrado a Azure, terraform apply OK | Sprints documentados | Contenedor arranca pero API no responde |
| 05/05 | Documentación completa | Vídeo en preparación | — |

---

## Sprint Review

**Demostrado:**
1. terraform plan mostrando 2 recursos a crear
2. terraform apply completado en 68 segundos
3. Resource Group rg-abc-analytics visible en Azure portal
4. Contenedor sales-prediction-api en estado Running

**Pendiente:** Imagen Docker personalizada en Azure Container Registry.

---

## Métricas del Sprint

- **Velocidad:** 12 puntos
- **Recursos Terraform creados:** 2
- **Tiempo terraform apply:** 68 segundos
- **Cobertura de tests final:** 75%
- **Tiempo total del proyecto:** ~20 horas por persona