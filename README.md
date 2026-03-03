# 🧠 Plantillas Profesionales de Proyecto  
## PHP · Python · Arduino · Perl · Power BI · Business Central

Este repositorio contiene **plantillas base listas para usar** para comenzar proyectos bien estructurados, seguros y con integración continua desde el primer momento.

La idea es simple:

> **No empezar nunca más un proyecto “desde cero” sin reglas, sin pruebas y sin seguridad.**

Aquí encontrarás carpetas independientes. Solo tienes que elegir la que necesites, copiarla o subirla como nuevo repositorio en GitHub… y empezar a trabajar.

---

# 📁 Estructura del repositorio

## 🔵 /PHP

Plantilla lista para proyectos **PHP + MySQL**.

Pensada para:

- Aplicaciones web  
- APIs REST  
- Paneles administrativos  
- Proyectos backend  
- Sistemas con base de datos MySQL  
- Código personalizado de WordPress (plugins, themes, mu-plugins)  

Incluye:

- Estructura de carpetas profesional  
- `agent.md` con reglas claras (seguridad, comentarios, testing, documentación)  
- RepoGuardian (informe accionable en PR + bloqueo de merge si lo activas)  
- `info.md` por carpeta (documentación viva)  
- `version.md` (registro de cambios)  

### ¿Qué aporta esta plantilla?

- Evita SQL Injection (consultas preparadas obligatorias)  
- Obliga a documentar y testear  
- Evita que se rompa producción sin avisar  
- Mantiene disciplina incluso si colaboran agentes IA  

---

## 🟢 /Python

Plantilla lista para proyectos en **Python**.

Pensada para:

- Automatizaciones  
- Herramientas internas  
- Aplicaciones de escritorio  

Incluye:

- Estructura profesional  
- `agent.md` con reglas de seguridad y testing  
- RepoGuardian + documentación viva  

---

## 🟠 /Arduino

Plantilla para proyectos con **Arduino**.

Pensada para:

- Domótica  
- Sensores  
- Automatización  

Incluye:

- Estructura organizada  
- Documentación obligatoria (pines, cableado, riesgos)  
- RepoGuardian + control de cambios  

---

## 🟣 /Perl

Plantilla lista para proyectos **Perl**.

Pensada para:

- Scripts y automatización  
- Herramientas CLI  
- Integraciones y sincronizaciones  

Incluye:

- Tests con `Test::More` / `prove`  
- `agent.md` con reglas de seguridad, documentación y disciplina  
- RepoGuardian + documentación viva  

---

## 🟡 /PowerBI-DAX

Plantilla para proyectos **Power BI** centrados en **DAX**.

Pensada para:

- Medidas DAX y KPIs documentados  
- Modelos semánticos con trazabilidad  
- Revisión seria en Pull Requests  

Incluye:

- Estructura para medidas y documentación del modelo  
- `agent.md` con reglas de modelado y seguridad de datos  
- RepoGuardian para obligar documentación y control de cambios  

---

## 🔷 /BusinessCentral-AL

Plantilla para **Microsoft Dynamics 365 Business Central (AL)**.

Pensada para:

- Extensiones AL  
- Personalizaciones con control de permisos y documentación  

Incluye:

- Estructura para objetos AL y documentación  
- `agent.md` con reglas de seguridad (mínimo privilegio) y disciplina  
- RepoGuardian + versionado de cambios  

---

# 🛡 RepoGuardian (cómo funciona)

RepoGuardian se ejecuta en Pull Requests y genera un informe en:

- Un comentario en el PR  
- El Step Summary del workflow  
- Un artefacto descargable  

Puede bloquear el merge si lo configuras como “status check” obligatorio.

### Reglas principales:

- No se puede subir `.env`.  
- Si cambias `src/`, debes cambiar `tests/` (cuando aplique).  
- Si cambias código o artefactos relevantes, debes actualizar `version.md`.  
- Si hay cambios dentro de una carpeta, debes actualizar su `info.md`.  

---

# ✅ Activar el bloqueo del merge

GitHub → **Settings** → **Branches** → **Branch protection rules**

Activa:

- Require a pull request before merging  
- Require status checks to pass before merging  
- Selecciona: `RepoGuardian - Cumplimiento agent.md`  

---

# 🎯 ¿Por qué este repositorio es útil?

Porque el mayor enemigo de un proyecto no es el bug grande.

Es el caos pequeño acumulado.

Este repositorio te da:

- Seguridad desde el inicio  
- Tests que explican qué está mal  
- CI / RepoGuardian que bloquea errores  
- Documentación obligatoria  
- Estructura clara  
- Normas coherentes para humanos y para IA  

---

# 🧩 Filosofía del repositorio

Este repositorio no es solo un conjunto de archivos.

Es una forma de trabajar.

Define reglas claras para:

- Cómo se escribe  
- Cómo se documenta  
- Cómo se prueba  
- Cómo se protege  
- Cómo se publica  
