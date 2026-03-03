# 🔵 Plantilla Profesional PHP + MySQL

Esta plantilla está pensada para iniciar proyectos PHP de forma seria, segura y mantenible desde el primer día.

No es solo una estructura de carpetas.

Es una forma de trabajar.

---

## 🎯 ¿Para qué tipo de proyectos sirve?

- Aplicaciones web
- APIs REST
- Backends con MySQL
- Paneles administrativos
- Sistemas internos
- Proyectos WordPress personalizados
- Plugins o desarrollos a medida sobre WordPress

Si tu stack es **PHP + MySQL**, esta es tu base.

---

## 📁 Estructura del proyecto

### /src
Aquí vive el código de tu aplicación.

Reglas:
- Código modular
- Clases con responsabilidad clara
- Consultas siempre con sentencias preparadas
- Nada de lógica mezclada con HTML si no es estrictamente necesario

Si modificas algo dentro de `src/`, debes:
- Actualizar `tests/`
- Actualizar `version.md`
- Actualizar `src/info.md`

---

### /tests
Pruebas unitarias y de regresión.

Si cambias lógica de negocio, debes añadir o modificar tests.

El objetivo no es “tener tests”.
El objetivo es que cuando algo se rompa, el error diga exactamente qué está mal.

---

### /docs
Documentación técnica y funcional.

Aquí se documenta:
- Estructura de base de datos
- Endpoints
- Decisiones arquitectónicas
- Flujo del sistema

Si algo cambia y afecta al comportamiento del sistema, debe reflejarse aquí.

---

### /scripts
Scripts auxiliares del proyecto.

Incluye:
- RepoGuardian (validador automático del PR)
- Scripts internos si los necesitas

---

## 🛡 Seguridad aplicada por agent.md

El `agent.md` define reglas obligatorias para mantener el código seguro:

- Uso obligatorio de sentencias preparadas (PDO)
- Prohibido concatenar variables en SQL
- Validación y sanitización de entrada
- Escape correcto en salida HTML
- Medidas anti-CSRF en formularios
- Prohibido subir `.env`
- Separación de responsabilidades
- Manejo controlado de errores (sin exponer trazas en producción)

---

## 🛡 RepoGuardian (qué hace)

RepoGuardian revisa cada Pull Request y valida:

- No se sube `.env`
- Si cambia `src/`, deben cambiar `tests/`
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

## 🧩 ¿Funciona con WordPress?

Sí.

El agente y RepoGuardian funcionan en proyectos WordPress para tu código personalizado:

- Plugins personalizados
- Themes desarrollados a medida
- Integraciones con base de datos

Qué contempla (cuando aplica):
- Sanitización con funciones nativas (por ejemplo `sanitize_text_field`, `esc_html`, `wp_kses`)
- Nonces en formularios y acciones (`wp_nonce_*`)
- Uso correcto de `$wpdb->prepare()`
- Revisión de capacidades (`current_user_can`)
- Evitar exponer configuración/credenciales (wp-config.php no debe subirse con secretos)

No interfiere con el core de WordPress. Aplica disciplina sobre tu código.

---

## 🚀 Filosofía

El objetivo no es complicar el desarrollo.

Es evitar el caos pequeño acumulado.

Si empieza bien estructurado, crecerá sin romperse.
