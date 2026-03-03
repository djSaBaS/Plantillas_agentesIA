# 🔷 Plantilla Profesional Business Central (AL)

Esta plantilla está pensada para iniciar extensiones de Microsoft Dynamics 365 Business Central (AL) de forma seria, segura y mantenible desde el primer día.

No es solo una estructura de carpetas.

Es una forma de trabajar.

---

## 🎯 ¿Para qué tipo de proyectos sirve?

- Extensiones AL
- Personalizaciones y módulos
- Proyectos con despliegue controlado y trazabilidad

Si tu stack es **Business Central + AL**, esta es tu base.

---

## 📁 Estructura del proyecto

### /src
Aquí viven los objetos AL (tablas, páginas, codeunits, reportes, etc.).

Si modificas algo dentro de `src/`, debes:
- Actualizar `version.md`
- Actualizar `src/info.md`
- Actualizar `tests/` cuando aplique

---

### /tests
Pruebas cuando aplique / cuando se configure el framework.

Si se corrige un bug y es viable, se debe añadir un test de regresión.

---

### /docs
Documentación funcional y técnica.

Aquí se documenta:
- Propósito de objetos y flujos
- Eventos y suscripciones
- Permisos y roles
- Impactos en datos

Si algo cambia y afecta al comportamiento, debe reflejarse aquí.

---

### /scripts
Scripts auxiliares del proyecto.

Incluye:
- RepoGuardian (validador automático del PR)

---

## 🛡 Seguridad aplicada por agent.md

El `agent.md` define reglas obligatorias:

- Principio de mínimo privilegio (permisos)
- Validación de estados/entradas en procesos
- Manejo controlado de errores
- Prohibido subir secretos

---

## 🛡 RepoGuardian (qué hace)

RepoGuardian revisa cada Pull Request y valida:

- No se sube `.env` (ni secretos)
- Si cambia código/objetos, debe actualizarse `version.md`
- Si cambia una carpeta, debe actualizarse su `info.md`
- Si cambia `src/`, `tests/` debe actualizarse cuando aplique

Publica un informe en el PR indicando qué falta y cómo arreglarlo.

---

## 🔒 Cómo activar el bloqueo del merge

GitHub → Settings → Branches → Branch protection rules

Activa:
- Require pull request before merging
- Require status checks to pass
- Marca: `RepoGuardian - Cumplimiento agent.md`

---

## 🚀 Filosofía

El objetivo no es complicar Business Central.

Es evitar que una extensión crezca sin control.

Si empieza bien documentado y con disciplina, se mantiene sin romperse.
