# agent.md

## 1. Propósito del proyecto

Este repositorio está diseñado para ser mantenido por desarrolladores humanos y por agentes de inteligencia artificial.

El objetivo es garantizar un desarrollo:

- Consistente  
- Seguro  
- Testeable (cuando aplique)  
- Escalable  
- Fácil de mantener a largo plazo  

Principios irrenunciables (orden de prioridad):

1) Seguridad  
2) Estabilidad  
3) Claridad del código  
4) Mantenibilidad  
5) Automatización de calidad (CI + validaciones)

La seguridad nunca se negocia.

---

## 2. Idioma obligatorio

Todo el contenido del repositorio debe estar en español:

- Comentarios del código  
- Documentación  
- Mensajes de commit  
- Archivos Markdown  
- Mensajes de error personalizados (cuando aplique)

---

## 3. Tipo de proyecto

Este repositorio es exclusivamente de tipo:

**Microsoft Dynamics 365 Business Central (AL)**

No se permite mezclar backend alternativo aquí. Si existen integraciones, se documenta el contrato en `/docs` y el componente vive fuera del repo.

---

## 4. Normas generales de desarrollo

### 4.1 Claridad del código

- El código debe ser explícito y comprensible.
- Evitar abreviaturas crípticas.
- Prohibido introducir complejidad innecesaria.
- No eliminar objetos/lógica sin verificar su uso real.
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

### 4.3 Documentación profesional de objetos

Utiliza sintaxis de Comentarios XML comentarios XML para documentar funciones. 

Los objetos AL (tablas, páginas, codeunits, reportes, etc.) deben documentarse:

- Propósito funcional
- Dependencias
- Eventos suscritos/publicados
- Impacto en permisos
- Consideraciones de seguridad

La documentación vive en `/docs` y debe actualizarse con cada cambio.

---

## 5. Seguridad (PRIORIDAD ABSOLUTA)

- Principio de mínimo privilegio: permisos estrictamente necesarios y documentados.
- Validar entradas y estados, especialmente en procesos que modifican datos.
- Manejo de errores controlado (sin filtrar información sensible).
- Revisar impactos en auditoría/registro cuando aplique.

---

### 5.1 Gestión de secretos

- Prohibido subir credenciales, tokens o claves.
- Conexiones y secretos se gestionan fuera del repositorio.

---

## 6. Calidad de código (sin alertas)

El proyecto debe mantenerse sin alertas críticas en:

- CI
- Reglas del entorno AL (cuando se configuren)

No se permite introducir advertencias nuevas sin justificación.

---

## 7. Estructura y documentación viva

Estructura base:

- `/src`: objetos AL
- `/tests`: pruebas (si aplica / cuando se configure)
- `/docs`: documentación funcional y técnica
- `/scripts`: scripts auxiliares (incluye RepoGuardian)

Cada carpeta de primer nivel debe contener `info.md` actualizado.

Si se modifica contenido dentro de una carpeta, debe actualizarse su `info.md`.

`version.md` debe actualizarse cuando haya cambios de código/objetos.

---

## 8. Testing (cuando aplique)

- Si se configura test framework, se deben añadir tests para objetos y lógica relevante.
- Cada bug corregido añade un test de regresión cuando sea viable.

Los tests deben fallar con mensajes accionables.

El CI debe bloquear merges si fallan las validaciones configuradas.

---

## 9. RepoGuardian

RepoGuardian valida en cada Pull Request:

- No se suben secretos.
- Si cambia `src/`, deben cambiar `tests/` cuando aplique.
- Si cambia código/objetos, debe actualizarse `version.md`.
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

- No cambiar permisos sin documentar impacto.
- No renombrar objetos sin justificar impacto y actualizar documentación.
- No introducir dependencias nuevas sin motivación.
- Priorizar cambios pequeños, revisables y con documentación.

El agente debe actuar como desarrollador senior responsable.
