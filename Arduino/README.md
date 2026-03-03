# 🟠 Plantilla Profesional Arduino

Plantilla para proyectos Arduino con estructura, control de calidad y disciplina documental.

Sí, incluso en hardware.

---

## 🎯 ¿Para qué tipo de proyectos sirve?

- Domótica
- Automatización
- Control de motores
- Sensores
- Sistemas embebidos
- Proyectos con relés, ventiladores, resistencias, etc.

---

## 📁 Estructura del proyecto

### /src
Sketches y código del microcontrolador.

Reglas:
- Código organizado
- Separación de lógica y control de pines
- Comentarios claros en cada bloque crítico

Si modificas:
- Actualiza `version.md`
- Actualiza `src/info.md`

---

### /docs
Aquí se documenta:
- Pinout
- Cableado
- Esquema lógico
- Medidas de seguridad eléctrica
- Voltajes y consumo

Si el cableado cambia, debe documentarse.

---

### /tests
Si aplica (por ejemplo lógica desacoplada).

---

### /scripts
Incluye RepoGuardian.

---

## 🛡 Seguridad aplicada por agent.md

El agente contempla:

- Documentación obligatoria de pines
- Comentarios explicativos en lógica crítica
- Evitar delays bloqueantes cuando el sistema lo requiera
- Definir constantes en lugar de números mágicos
- Documentar riesgos eléctricos
- Separar configuración de lógica

No sustituye pruebas físicas.
Pero reduce errores antes de cargar el sketch.

---

## 🛡 RepoGuardian

Valida en cada PR:

- Documentación actualizada
- version.md actualizado
- info.md actualizado en carpetas modificadas
- Disciplina estructural del proyecto

---

## 🔒 Activar bloqueo

GitHub → Settings → Branches → Branch protection rules

Activar:
- Require pull request
- Require status checks
- Seleccionar `RepoGuardian - Cumplimiento agent.md`

---

## 🚀 Filosofía

Muchos proyectos Arduino fallan por improvisación.

Esta plantilla obliga a pensar antes de conectar.

Y pensar antes de conectar ahorra placas quemadas.