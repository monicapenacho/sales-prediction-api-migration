# Guía de Presentación — ABC Analytics Migration
## Esquema diapositiva a diapositiva (15-20 minutos)

**Asignatura:** Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos (20GIAR)  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Proyecto:** Proyecto 3 — Migración Cloud  
**Fecha:** 6 de mayo de 2026

---

## Lo básico

- **Tiempo:** 15-20 minutos de presentación
- **Diapositivas:** máximo 15 (1 diapositiva ≈ 1 minuto)
- **Herramienta:** PowerPoint, Google Slides o Canva
- **Regla de oro:** Si lo que decís está en la diapositiva, no hace falta que lo leáis
- **Demo obligatoria:** pipeline en verde en GitHub Actions + API en Azure
- **Si es vídeo:** presentación individual

---

## Estructura completa (13 diapositivas, ~17 minutos)

---

### DIAPOSITIVA 1 — Portada (0:00 – 0:30)

**Qué poner:**
- Nombre del proyecto
- Los dos nombres del equipo
- Proyecto elegido (Proyecto 3 — Migración Cloud)
- Fecha y asignatura

**Qué decir:**
> "Buenos días. Somos Juan Manuel Campos y Mónica Penacho, y vamos a presentar
> la migración cloud de ABC Analytics, una API de predicción de ventas que hemos
> migrado desde servidores on-premise a Azure usando Docker, Terraform y GitHub Actions."

---

### DIAPOSITIVA 2 — El problema (0:30 – 2:00)

**Qué poner:**
- El problema de negocio en lenguaje simple
- Limitaciones de la infraestructura on-premise
- Por qué es urgente migrar

**Qué decir:**
> "ABC Analytics tiene una API de predicción de ventas en servidores físicos on-premise.
> El problema es triple: no puede escalar cuando hay picos de demanda, los despliegues
> son manuales y propensos a errores, y el coste de mantenimiento del hardware es fijo
> independientemente del uso. La solución es migrar a la nube."

---

### DIAPOSITIVA 3 — Estrategia de migración (2:00 – 3:30)

**Qué poner:**
- Las 6R de migración cloud vistas en clase
- Cuál hemos elegido y por qué (Rehost + Replatform)
- Comparativa on-premise vs cloud

**Qué decir:**
> "Siguiendo las 6R de migración cloud que vimos en clase, hemos optado por una
> estrategia de Rehosting con modernización parcial: containerizamos la aplicación
> con Docker y la desplegamos en Azure Container Instances, modernizando el framework
> a FastAPI sin reescribir la lógica de negocio."

---

### DIAPOSITIVA 4 — Arquitectura (3:30 – 6:00)

**Qué poner:**
- Diagrama de arquitectura completo
- Flujo desde el código hasta Azure
- Capas: GitHub → CI/CD → Azure

**Qué decir:**
> "La arquitectura tiene tres capas. La primera es el repositorio GitHub, que actúa
> como centro de control. La segunda son los dos jobs del pipeline: CI para calidad
> del código y CD para el despliegue. La tercera es Azure, donde corre la API en
> producción en un contenedor con IP pública."

**Preguntas que el profesor VA A HACER:**
- "¿Por qué dos jobs y no uno?" → CI en todas las ramas para detectar errores pronto;
  CD solo en principal para evitar despliegues accidentales
- "¿Por qué Azure y no AWS?" → AWS Educate no da acceso a servicios reales de
  infraestructura; Azure Students ofrece 100$ de crédito con el correo universitario
- "¿Cuánto cuesta esto al mes?" → ~8.50€/mes en Azure Students

---

### DIAPOSITIVA 5 — Tecnologías (6:00 – 7:00)

**Qué poner:**
- Tabla de tecnologías con justificación

| Componente | Tecnología | Por qué |
|------------|-----------|---------|
| API | FastAPI | Más rápido que Flask; Swagger automático |
| Contenedor | Docker | Reproducibilidad; estándar del sector |
| CI/CD | GitHub Actions | Integrado con el repo; visto en clase |
| Cloud | Azure | Trabajado en clase; cuenta estudiante |
| IaC | Terraform | Multi-cloud; reproducible; visto en clase |

---

### DIAPOSITIVA 6 — Demo CI/CD (7:00 – 9:00)

**OBLIGATORIA**

**Qué mostrar:**
1. Historial de commits en GitHub Actions
2. Pipeline en verde ✅ con los dos jobs
3. Log de tests con cobertura 75%

**Qué decir:**
> "Cada vez que hacemos push al repositorio, el pipeline se dispara automáticamente.
> Primero ejecuta el lint con ruff y los tests con pytest, verificando que la cobertura
> es mayor del 70%. Solo si todo pasa, el segundo job construye la imagen Docker y la
> sube a Azure Container Registry."

---

### DIAPOSITIVA 7 — Demo Terraform + Azure (9:00 – 11:00)

**Qué mostrar:**
1. Captura del terraform plan con los 2 recursos
2. Captura del terraform apply completado en 68 segundos
3. Portal Azure con el Resource Group y el contenedor en Running

**Qué decir:**
> "Con un solo comando, terraform apply, creamos toda la infraestructura en Azure
> en 68 segundos. Se crean automáticamente el grupo de recursos y el contenedor
> con IP pública. Si borramos todo por error, lo recuperamos en menos de 2 minutos."

---

### DIAPOSITIVA 8 — Código relevante (11:00 – 12:00)

**Qué mostrar:**
- Snippet 1: endpoint /predict de la API
- Snippet 2: job CI/CD del workflow
- Snippet 3: resource azurerm_container_group de Terraform

**Regla de oro:** No leer el código línea a línea. Explicar el QUÉ hace y el POR QUÉ.

---

### DIAPOSITIVA 9 — Métricas (12:00 – 13:00)

**Qué poner:**

| Métrica | Objetivo | Resultado |
|---------|----------|-----------|
| Cobertura tests | ≥ 70% | 75% ✅ |
| Pipeline CI/CD | Verde en cada push | ✅ |
| Terraform apply | Reproducible | 68 seg ✅ |
| Contenedor Azure | Running | ✅ Spain Central |

---

### DIAPOSITIVA 10 — Metodología ágil (13:00 – 14:30)

**Qué poner:**
- Tabla resumen de los 3 sprints
- Velocidad del equipo
- Captura del tablero Scrum

| Sprint | Objetivo | Puntos |
|--------|----------|--------|
| Sprint 1 | API + Docker + Tests | 13/13 ✅ |
| Sprint 2 | CI/CD + Cobertura | 13/13 ✅ |
| Sprint 3 | Terraform + Azure | 12/16 🔄 |

**Qué decir:**
> "Trabajamos con Scrum y sprints de 2 semanas. La comunicación entre el equipo
> fue clave para resolver los impedimentos rápidamente. Por ejemplo, el problema
> de permisos de Terraform se resolvió en pocas horas gracias a la comunicación directa."

---

### DIAPOSITIVA 11 — Dificultades encontradas (14:30 – 15:30)

**Qué poner:**
- Los problemas reales que encontramos
- Cómo los resolvimos

| Dificultad | Solución |
|-----------|----------|
| AWS Educate no funciona | Migrar a Azure Students |
| Terraform sin permisos | skip_provider_registration |
| Pipeline fallaba por nombres en español | Corregir rutas en ci.yml |
| ModuleNotFoundError en tests | __init__.py + PYTHONPATH |

---

### DIAPOSITIVA 12 — ¿Qué haríamos diferente? (15:30 – 16:30)

> Esta diapositiva demuestra madurez técnica — muy valorada por el profesor.

**Lo que no haríamos de nuevo:**
1. Intentar usar AWS sin verificar los permisos antes
2. No configurar los secrets de ACR desde el Sprint 1
3. No haber puesto Branch Protection Rules desde el inicio

**Lo que añadiríamos:**
1. Azure Container Registry con imagen Docker personalizada
2. Azure Monitor para observabilidad completa
3. Estrategia de despliegue Canary

---

### DIAPOSITIVA 13 — Conclusiones y preguntas (16:30 – 17:30)

**3 conclusiones:**
1. Terraform hace la infraestructura reproducible: recrear el entorno tarda 68 segundos
2. El pipeline CI/CD detectó errores automáticamente antes de llegar a producción
3. La metodología Scrum permitió organizar el trabajo con objetivos claros por sprint

**Qué poner al final:** enlace al repositorio GitHub

---

## Preguntas frecuentes del profesor

**1. "¿Por qué Azure y no AWS?"**
→ AWS Educate solo da acceso a cursos, no a servicios reales. Azure Students ofrece
100$ de crédito con el correo de la universidad, sin tarjeta de crédito.

**2. "¿Por qué dos jobs en el pipeline y no uno?"**
→ El CI se ejecuta en todas las ramas para detectar errores pronto. El CD solo en
principal y solo si el CI pasa, evitando despliegues accidentales.

**3. "¿Cuánto cuesta esto al mes?"**
→ ~8.50€/mes en Azure. Container Instances ~3.50€ + Container Registry ~5€.

**4. "¿Por qué FastAPI y no Flask?"**
→ FastAPI es más rápido, tiene documentación automática con Swagger y validación
de datos con Pydantic incluida.

**5. "¿Por qué Terraform y no desplegar manualmente desde el portal de Azure?"**
→ Terraform garantiza reproducibilidad e idempotencia. Si borramos la infraestructura
por error, la recuperamos en 68 segundos con terraform apply.

---

## Errores que hay que evitar

| Error | Cómo evitarlo |
|-------|---------------|
| Explicar el código línea a línea | Explicar el QUÉ y el POR QUÉ |
| No mencionar los problemas reales | Contar AWS Educate, permisos Terraform, etc. |
| No hacer demo | Practicar la demo 5+ veces antes |
| Excederse del tiempo | Cronometrar el ensayo mínimo 2 veces |

---

## Timings de referencia

| Diapositiva | Tema | Tiempo |
|-------------|------|--------|
| 1 | Portada | 0:30 |
| 2 | El problema | 1:30 |
| 3 | Estrategia migración | 1:30 |
| 4 | Arquitectura | 2:30 |
| 5 | Tecnologías | 1:00 |
| 6 | Demo CI/CD | 2:00 |
| 7 | Demo Terraform + Azure | 2:00 |
| 8 | Código relevante | 1:00 |
| 9 | Métricas | 1:00 |
| 10 | Metodología ágil | 1:30 |
| 11 | Dificultades | 1:00 |
| 12 | ¿Qué haríamos diferente? | 1:00 |
| 13 | Conclusiones + preguntas | 1:00 |
| **TOTAL** | | **~17 minutos** |