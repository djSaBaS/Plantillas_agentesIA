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

**Perl**

Se permite incluir HTML/CSS/JS si forma parte del artefacto final (por ejemplo, plantillas o assets), pero no se permite introducir un backend alternativo en otro lenguaje sin una arquitectura formalmente documentada que lo justifique.

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

### 4.3 Documentación profesional de funciones y módulos

Las funciones (subrutinas) y módulos deben documentarse con estándar profesional:

- Preferiblemente POD (Plain Old Documentation) para módulos y scripts principales.

La documentación debe incluir:

- Descripción clara
- Parámetros
- Retorno
- Errores relevantes
- Consideraciones de seguridad si aplica

No se aceptan subrutinas críticas sin documentación.

---

## 5. Seguridad (PRIORIDAD ABSOLUTA)

Nunca confiar en entradas externas.

Reglas obligatorias:

- Validar, normalizar y sanear toda entrada (CLI, ficheros, red, variables de entorno).
- Prohibido ejecutar comandos construidos con entradas no validadas.
- Evitar interpolación peligrosa en llamadas a sistema.
- No exponer stack traces ni detalles internos en mensajes de error.
- No registrar secretos en logs.

---

### 5.1 Gestión de secretos

- Debe existir `.env.example` cuando aplique.
- `.env` debe estar en `.gitignore`.
- Prohibido subir secretos.
- El CI debe incluir escaneo de secretos cuando aplique.

---

## 6. Calidad de código (sin alertas)

El proyecto debe mantenerse sin alertas críticas en:

- Linting (si se configura)
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

- Tests unitarios para funciones y módulos.
- Tests de regresión para cada bug corregido.

Herramientas recomendadas:
- `Test::More`
- Ejecución con `prove`.

Los tests deben fallar con mensajes accionables:

- Qué caso falló.
- Qué se esperaba.
- Qué se obtuvo.
- Qué debe corregirse.

El CI debe bloquear merges si fallan tests.

---

## 9. RepoGuardian

RepoGuardian valida en cada Pull Request:

- No se suben secretos.
- Si cambia `src/`, deben cambiar `tests/` (cuando aplique).
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
