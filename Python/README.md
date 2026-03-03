# 🟢 Plantilla Profesional Python

Plantilla base para proyectos Python estructurados, testeados y con control automático de calidad.

No importa si es un script pequeño.
Empieza profesional.

---

## 🎯 ¿Para qué tipo de proyectos sirve?

- Aplicaciones de escritorio
- Automatizaciones
- Microservicios
- Scripts internos
- Procesamiento de datos
- Proyectos que terminarán en ejecutable (.exe)

---

## 📁 Estructura del proyecto

### /src
Código fuente del proyecto.

Reglas:
- Funciones con responsabilidad clara
- Tipado cuando sea posible
- Separación lógica de módulos
- Nada de lógica global descontrolada

Si cambias algo aquí:
- Debes modificar `tests/`
- Debes actualizar `version.md`
- Debes actualizar `src/info.md`

---

### /tests
Pruebas unitarias.

No son decorativas.

Deben explicar qué falla si algo se rompe.

---

### /docs
Documentación del sistema:
- Arquitectura
- Flujos
- Decisiones técnicas

---

### /scripts
Incluye RepoGuardian y scripts auxiliares.

---

## 🛡 Seguridad aplicada por agent.md

El agente define:

- No ejecutar código dinámico inseguro (eval, exec sin control)
- Validación de entrada
- Manejo controlado de excepciones
- No exponer secretos en repositorio
- Uso seguro de subprocess
- Control de dependencias externas

---

## 🛡 RepoGuardian

Valida automáticamente en cada PR:

- No se suben secretos
- Tests obligatorios si cambia código
- version.md actualizado
- info.md actualizado en carpetas modificadas

Genera un informe accionable en el PR.

---

## 🔒 Activar bloqueo de merge

GitHub → Settings → Branches → Branch protection rules

Activar:
- Require pull request
- Require status checks
- Seleccionar `RepoGuardian - Cumplimiento agent.md`

---

## 🚀 Filosofía

Un script sin estructura crece mal.

Un script estructurado puede convertirse en sistema.

Empieza con orden.