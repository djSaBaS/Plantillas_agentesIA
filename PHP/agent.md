# agent.md

## 1. Propósito del proyecto

Este repositorio está diseñado para ser mantenido por desarrolladores humanos y por agentes de inteligencia artificial.

El objetivo es garantizar un desarrollo:

- Consistente  
- Seguro  
- Testeable  
- Escalable  
- Fácil de mantener a largo plazo  

Principios irrenunciables (orden de prioridad):

1) Seguridad  
2) Estabilidad  
3) Claridad del código  
4) Mantenibilidad  
5) Automatización de calidad (CI + tests)

La seguridad nunca se negocia.

---

## 2. Idioma obligatorio

Todo el contenido del repositorio debe estar en español:

- Comentarios del código  
- Documentación  
- Mensajes de commit  
- Archivos Markdown  
- Mensajes de error personalizados  

La coherencia lingüística es parte de la calidad del proyecto.

---

## 3. Tipo de proyecto

Este repositorio es exclusivamente de tipo:

**PHP + MySQL**

No se permite mezclar tecnologías de otros tipos de repositorio.

Si el proyecto es WordPress, estas reglas aplican únicamente al código personalizado (plugins, themes, mu-plugins).

---

## 4. Normas generales de desarrollo

### 4.1 Claridad del código

- El código debe ser explícito y comprensible.
- Evitar abreviaturas crípticas.
- Prohibido introducir complejidad innecesaria.
- No eliminar código sin verificar su uso real.
- No aplicar refactors masivos sin justificación.

El código debe poder leerse dentro de seis meses sin necesidad de explicación adicional.

---

### 4.2 Comentarios obligatorios (línea a línea)

Todo el código debe estar comentado línea a línea:

- El comentario va en la línea anterior.
- No usar prefijos como “Comentario:”.
- El comentario debe explicar qué hace la línea o por qué existe.
- Priorizar explicar el “por qué” frente al “qué”.

Excepción:
- Líneas autoexplicativas dentro de bloques ya documentados.

---

### 4.3 Documentación profesional de funciones y clases

Todas las funciones, clases y métodos deben documentarse usando PHPDoc.

Debe incluir:

- Descripción clara
- Parámetros (tipo y descripción)
- Tipo de retorno
- Posibles excepciones
- Consideraciones de seguridad si aplica

No se aceptan funciones sin documentación.

---

## 5. Seguridad (PRIORIDAD ABSOLUTA)

Nunca confiar en entradas externas.

Reglas obligatorias:

- Validar, normalizar y sanear toda entrada.
- Prohibido concatenar SQL con datos del usuario.
- Uso obligatorio de PDO con consultas preparadas.
- Escapar toda salida HTML.
- Implementar protección anti-CSRF en formularios.
- No exponer stack traces en producción.
- No exponer estructura interna en mensajes de error.
- Aplicar principio de mínimo privilegio en acceso a base de datos.

---

### 5.1 Gestión de secretos

- Debe existir `.env.example`.
- `.env` debe estar en `.gitignore`.
- Prohibido subir secretos.
- El CI debe incluir escaneo de secretos cuando aplique.

---

### 5.2 WordPress (si aplica)

Cuando el proyecto sea WordPress:

- Sanitización con funciones nativas (`sanitize_text_field`, etc.).
- Escape correcto (`esc_html`, `wp_kses`, etc.).
- Uso obligatorio de nonces (`wp_nonce_*`) en acciones sensibles.
- Validación de capacidades (`current_user_can`).
- Consultas SQL mediante `$wpdb->prepare()`.
- Nunca modificar el core.

RepoGuardian y estas normas aplican solo al código personalizado.

---

## 6. Calidad de código (sin alertas)

El proyecto debe mantenerse sin alertas críticas en:

- Análisis estático
- Linting
- CI

No se permite introducir advertencias nuevas sin justificación.

---

## 7. Estructura y documentación viva

Estructura base:

- `/src`
- `/tests`
- `/docs`
- `/scripts`

Cada carpeta de primer nivel debe contener `info.md` actualizado.

Si se modifica contenido dentro de una carpeta, debe actualizarse su `info.md`.

`version.md` debe actualizarse cuando haya cambios de código.

---

## 8. Testing obligatorio

- Tests unitarios para funciones y clases.
- Tests de regresión para cada bug corregido.
- Tests de integración cuando aplique.

Los tests deben fallar con mensajes accionables:

- Qué caso falló.
- Qué se esperaba.
- Qué se obtuvo.
- Qué debe corregirse.

El CI debe publicar reportes y bloquear merges si fallan tests.

---

## 9. RepoGuardian

RepoGuardian valida en cada Pull Request:

- No se suben secretos.
- Si cambia `src/`, deben cambiar `tests/`.
- Si cambia código, debe actualizarse `version.md`.
- Si cambia una carpeta, debe actualizarse su `info.md`.

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

- No introducir dependencias nuevas sin justificar.
- No refactorizar masivamente sin necesidad.
- No eliminar código sin verificar uso y sin test.
- Priorizar cambios pequeños, revisables y testeados.
- No modificar arquitectura sin documentación previa en `/docs`.

El agente debe actuar como desarrollador senior responsable.