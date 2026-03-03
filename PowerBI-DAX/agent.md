# agent.md

## 1. Propósito del proyecto

Este repositorio está diseñado para ser mantenido por desarrolladores humanos y por agentes de inteligencia artificial.

El objetivo es garantizar un desarrollo:

- Consistente  
- Seguro  
- Trazable  
- Fácil de mantener a largo plazo  

Principios irrenunciables (orden de prioridad):

1) Seguridad (datos y accesos)  
2) Estabilidad del modelo  
3) Claridad (medidas, KPIs y documentación)  
4) Mantenibilidad  
5) Automatización de calidad (revisión en PR + CI)

La seguridad nunca se negocia.

---

## 2. Idioma obligatorio

Todo el contenido del repositorio debe estar en español:

- Documentación  
- Archivos Markdown  
- Descripciones de medidas/KPIs  
- Nombres y comentarios en artefactos exportados (cuando aplique)

---

## 3. Tipo de proyecto

Este repositorio es exclusivamente de tipo:

**Power BI (DAX)**

No se permite mezclar backend aquí. Si existe backend, debe vivir en otro repositorio. Aquí solo se documenta el contrato (inputs/outputs) si aplica.

---

## 4. Normas generales de desarrollo

### 4.1 Claridad del modelo

- Nombres de tablas, columnas y medidas coherentes y consistentes.
- Evitar abreviaturas crípticas.
- Mantener un diccionario de datos en `/docs`.

---

### 4.2 Medidas DAX (buenas prácticas)

- Evitar medidas “monstruo”: dividir en medidas auxiliares.
- Documentar el contexto de filtro esperado.
- Documentar supuestos (por ejemplo, moneda, calendario, granularidad).
- Evitar ambigüedad en relaciones y filtros.

---

### 4.3 Documentación de cada medida

Toda medida publicada debe documentarse con:

- Propósito
- Definición DAX
- Entradas (tablas/columnas que usa)
- Comportamiento esperado con filtros
- Casos límite conocidos
- Consideraciones de rendimiento si aplica

---

## 5. Seguridad (PRIORIDAD ABSOLUTA)

- Prohibido subir datos sensibles sin anonimización.
- Prohibido subir credenciales, tokens o cadenas de conexión.
- Prohibido subir exportaciones con información personal si no está permitido.

Requisitos:
- Documentar roles/accesos si aplica (RLS, permisos, etc.).

---

## 6. Calidad y consistencia

- Consistencia en nombres, formatos y KPIs.
- Si se cambia una definición (KPI), debe documentarse en `/docs` y reflejarse en `version.md`.
- Evitar medidas redundantes (preferir reutilización).

---

## 7. Estructura y documentación viva

Estructura base:

- `/src`: medidas, expresiones, artefactos exportables
- `/docs`: modelo, tablas, relaciones, KPIs, decisiones
- `/tests`: validaciones simples cuando aplique
- `/scripts`: scripts auxiliares (incluye RepoGuardian)

Cada carpeta de primer nivel debe contener `info.md` actualizado.

Si se modifica contenido dentro de una carpeta, debe actualizarse su `info.md`.

`version.md` debe actualizarse cuando haya cambios relevantes (medidas, KPIs, modelo).

---

## 8. Testing / validación (cuando aplique)

Power BI es principalmente visual. Aun así, se exige disciplina:

- Si se corrige un bug en un KPI/medida, debe quedar un caso reproducible documentado (inputs, filtros, resultado esperado).
- Si es viable, añadir una validación automatizada sencilla (por ejemplo, checks de consistencia sobre artefactos exportados).

El CI debe bloquear merges si falla lo que esté configurado.

---

## 9. RepoGuardian

RepoGuardian valida en cada Pull Request:

- No se suben secretos.
- Si cambia contenido relevante, debe actualizarse `version.md`.
- Si cambia una carpeta, debe actualizarse su `info.md`.
- Si cambia `src/`, `tests/` debe actualizarse cuando aplique.

Si está configurado como status check obligatorio, bloqueará el merge.

RepoGuardian no sustituye revisión humana. Refuerza disciplina estructural.

---

## 10. Flujo de trabajo Git

- `main` debe estar estable.
- Ramas: `feature/*`, `fix/*`, `docs/*`, `refactor/*`, `test/*`, `chore/*`.
- Recomendado: Conventional Commits.

No se hace merge directo a `main`.

---

## 11. Restricciones específicas para agentes IA

- No cambiar KPIs críticos sin documentarlo en `/docs` y `version.md`.
- No renombrar medidas/tablas sin justificar impacto.
- Priorizar cambios pequeños y revisables.
- No subir datos reales sensibles para “hacer pruebas”.

El agente debe actuar como desarrollador senior responsable.
