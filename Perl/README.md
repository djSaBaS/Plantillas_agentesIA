# 🟣 Plantilla Profesional Perl

Esta plantilla está pensada para iniciar proyectos Perl de forma seria, segura y mantenible desde el primer día.

No es solo una estructura de carpetas.

Es una forma de trabajar.

---

## 🎯 ¿Para qué tipo de proyectos sirve?

- Scripts y automatización
- Herramientas CLI
- Integraciones y sincronizaciones
- Procesos batch
- Servicios clásicos (cuando aplique)

Si tu stack es **Perl**, esta es tu base.

---

## 📁 Estructura del proyecto

### /src
Aquí vive el código del proyecto.

Reglas:
- Código modular (módulos cuando aplique)
- Subrutinas con responsabilidad clara
- Manejo de errores controlado
- Validación estricta de entradas

Si modificas algo dentro de `src/`, debes:
- Actualizar `tests/`
- Actualizar `version.md`
- Actualizar `src/info.md`

---

### /tests
Pruebas unitarias y de regresión con mensajes accionables.

El objetivo no es “tener tests”.
El objetivo es que cuando algo se rompa, el error diga exactamente qué está mal.

Recomendado:
- `Test::More`
- `prove`

---

### /docs
Documentación técnica y funcional.

Aquí se documenta:
- Flujo del sistema
- Contratos de integración (si los hay)
- Decisiones técnicas
- Riesgos y consideraciones de seguridad

---

### /scripts
Scripts auxiliares del proyecto.

Incluye:
- RepoGuardian (validador automático del PR)
- Scripts internos si los necesitas

---

## 🛡 Seguridad aplicada por agent.md

El `agent.md` define reglas obligatorias para mantener el código seguro:

- Validación y sanitización de entrada (CLI, ficheros, red)
- Prohibido ejecutar comandos con entradas no validadas
- Manejo controlado de errores (sin filtrar secretos)
- Prohibido subir `.env`
- Principio de mínimo privilegio

---

## 🛡 RepoGuardian (qué hace)

RepoGuardian revisa cada Pull Request y valida:

- No se sube `.env`
- Si cambia `src/`, deben cambiar `tests/` (cuando aplique)
- Si cambia código, debe actualizarse `version.md`
- Si cambia una carpeta, debe actualizarse su `info.md`

Publica un informe en el PR indicando qué falta y cómo arreglarlo.

---

## 🔒 Cómo activar el bloqueo del merge

GitHub → Settings → Branches → Branch protection rules

Activa:
- Require pull request before merging
- Require status checks to pass
- Marca: `RepoGuardian - Cumplimiento agent.md`

Ahora no se puede hacer merge si no se cumplen las reglas.

---

## 🚀 Filosofía

El objetivo no es complicar el desarrollo.

Es evitar el caos pequeño acumulado.

Si empieza bien estructurado, crecerá sin romperse.
