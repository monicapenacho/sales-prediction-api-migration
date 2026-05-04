# Sprint Retrospective — Sprint 3 (y Global del Proyecto)

**Fecha:** 06/05/2026  
**Equipo:** Juan Manuel Campos Enrique / Mónica Penacho  
**Formato:** Start / Stop / Continue

---

## ¿Qué fue bien? (Continue)

- **El pipeline CI/CD funcionó exactamente como se diseñó.** En el Sprint 2 detectó automáticamente errores de nombres de archivos y módulos no encontrados, evitando que código roto llegara a la rama principal.

- **Terraform demostró su valor para la reproducibilidad.** Recrear toda la infraestructura en Azure tardó 68 segundos con un solo comando. Sin Terraform, habría que configurar manualmente cada recurso en el portal de Azure.

- **La separación de CI y CD en jobs independientes.** El CD solo se ejecuta si el CI pasa y solo en la rama principal, evitando despliegues accidentales desde ramas de desarrollo.

- **Docker garantizó la portabilidad.** El mismo contenedor funciona en local y en Azure sin ningún cambio en el código.

---

## ¿Qué no funcionó? (Stop)

- **Subestimar los problemas de permisos en Azure.** La cuenta de estudiante tiene restricciones que no están documentadas claramente. En proyectos futuros, verificaríamos los permisos necesarios antes de empezar con Terraform.

- **No haber configurado los secrets de GitHub desde el inicio.** Los secrets de Azure Container Registry (ACR_LOGIN_SERVER, ACR_USERNAME, ACR_PASSWORD) se dejaron para el final, bloqueando el job de CD.

- **Intentar usar AWS cuando el curso se impartió con Azure.** AWS Educate no da acceso a servicios reales de infraestructura. Habríamos ahorrado tiempo yendo directamente a Azure Students.

---

## ¿Qué mejoraríamos? (Start)

- **Configurar Azure Container Registry desde el Sprint 1** para tener la imagen personalizada lista desde el principio.

- **Usar pre-commit hooks** para detectar errores de lint antes del push y evitar fallos en el pipeline CI.

- **Documentar las decisiones de arquitectura en el momento en que se toman**, no al final del proyecto cuando algunos detalles ya se han olvidado.

- **Configurar Branch Protection Rules** en GitHub desde el inicio, para requerir que el CI pase antes de poder hacer merge a la rama principal.

---

## Reflexión sobre la metodología ágil

**¿Sirvió SCRUM para este proyecto?**

Sí, con adaptaciones. Los sprints de 2 semanas fueron adecuados para el cronograma del proyecto. Lo más valioso fue tener un Sprint Goal claro en cada sprint: nos ayudó a priorizar y a no dispersarnos en tareas secundarias.

La comunicación entre los dos miembros del equipo fue clave para resolver los impedimentos rápidamente. Por ejemplo, el problema de permisos de Terraform en el Sprint 3 se resolvió en pocas horas gracias a la comunicación directa.

**¿Qué añadiríamos con más tiempo?**

- Un cuarto sprint dedicado a la imagen Docker personalizada en Azure Container Registry
- Implementación de Azure Monitor para observabilidad completa
- Estrategia de despliegue Canary para minimizar el riesgo en producción
- Autenticación con Azure Active Directory

---

## Velocidad por sprint

| Sprint | Puntos planificados | Puntos completados | % completado |
|--------|--------------------|--------------------|--------------|
| Sprint 1 | 13 | 13 | 100% |
| Sprint 2 | 13 | 13 | 100% |
| Sprint 3 | 16 | 12 | 75% |
| **Total** | **42** | **38** | **90%** |

---

## Lección más importante del proyecto

> "La infraestructura como código con Terraform y el pipeline CI/CD no son opcionales en un proyecto profesional — son la diferencia entre un despliegue reproducible y uno manual propenso a errores."