# agent.md

## 1. Propósito del proyecto

Este repositorio está diseñado para ser mantenido por desarrolladores humanos y por agentes de inteligencia artificial.

El objetivo es garantizar un desarrollo:

- Seguro (incluyendo seguridad eléctrica cuando aplique)  
- Estable  
- Comprensible  
- Mantenible  
- Documentado  
- Con validaciones automáticas cuando sea posible  

Principios irrenunciables (orden de prioridad):

1) Seguridad (eléctrica + lógica)  
2) Estabilidad del sistema  
3) Claridad del código  
4) Mantenibilidad  
5) Automatización de calidad (CI + pruebas cuando aplique)

En hardware, un error no solo rompe software: puede romper componentes.

---

## 2. Idioma obligatorio

Todo el contenido del repositorio debe estar en español:

- Comentarios del código  
- Documentación  
- Mensajes de commit  
- Archivos Markdown  

---

## 3. Tipo de proyecto

Este repositorio es exclusivamente de tipo:

**Arduino**

No se permite mezclar otras plataformas/lenguajes como backend dentro del mismo repositorio salvo que exista una arquitectura documentada (por ejemplo, una API externa consumida por el sistema o un panel web separado en otro repo).

---

## 4. Normas generales de desarrollo

### 4.1 Claridad del código

- Código explícito y legible.
- Evitar “magia” y atajos.
- Prohibido introducir complejidad sin necesidad.
- No eliminar código sin verificar uso y sin justificarlo.

---

### 4.2 Comentarios obligatorios (línea a línea)

Todo el código debe estar comentado línea a línea:

- Comentario en la línea anterior.
- Sin prefijos “Comentario:”.
- Explicar qué hace o por qué existe.
- Priorizar el “por qué” en lógica crítica (seguridad, estados, temporizaciones).

Excepción:
- Líneas autoexplicativas dentro de bloques ya documentados.

---

### 4.3 Documentación profesional de funciones y módulos

Todas las funciones relevantes deben tener cabecera de documentación indicando:

- Propósito
- Entradas/salidas
- Estados que afecta
- Consideraciones de seguridad
- Restricciones (timing, interrupciones, bloqueo/no bloqueo)

---

## 5. Seguridad (PRIORIDAD ABSOLUTA)

### 5.1 Seguridad eléctrica y de hardware (cuando aplique)

Debe documentarse en `/docs`:

- Pinout
- Cableado
- Voltajes (5V/3.3V)
- Consumo estimado
- Relés (tipo, aislamiento, protección)
- Medidas de protección recomendadas:
  - Optoacopladores si aplica
  - Fusibles si aplica
  - Diodos flyback en bobinas si aplica
  - Separación de potencia y señal

Si existe riesgo eléctrico, se prioriza la seguridad y se documenta.

---

### 5.2 Seguridad lógica

- Definir estados claros del sistema (máquina de estados cuando aplique).
- Evitar condiciones de carrera y estados ambiguos.
- Implementar “failsafe”:
  - Qué pasa si un sensor falla
  - Qué pasa si hay valores fuera de rango
  - Qué pasa si se pierde alimentación o reinicia
- Evitar números mágicos: constantes y enums.

---

## 6. Rendimiento y comportamiento no bloqueante

- Evitar `delay()` en sistemas que requieren respuesta simultánea o múltiples tareas.
- Preferir `millis()` y temporizadores no bloqueantes cuando aplique.
- Si se usa `delay()`, debe justificarse y documentarse.

---

## 7. Estructura y documentación viva

Estructura base:

- `/src`
- `/tests` (si aplica)
- `/docs`
- `/scripts`

Reglas:
- Cada carpeta de primer nivel debe contener `info.md` actualizado.
- Si se modifica contenido dentro de una carpeta, debe actualizarse su `info.md`.
- `version.md` debe actualizarse cuando haya cambios de código.

La documentación en Arduino no es opcional: es parte del funcionamiento.

---

## 8. Testing y validación

Arduino no siempre permite tests clásicos, pero se deben aplicar validaciones:

- Compilación automática en CI (obligatoria).
- Tests de lógica desacoplada si aplica (por ejemplo funciones puras).
- Checks de estilo y consistencia cuando sea posible.

Si se corrige un bug, debe documentarse y, si se puede, añadirse una validación que lo detecte.

---

## 9. RepoGuardian

RepoGuardian valida en cada Pull Request:

- Documentación actualizada (`info.md` por carpeta afectada).
- `version.md` actualizado cuando cambia código.
- Disciplina estructural del proyecto.
- No subir secretos (`.env` u otros ficheros sensibles si existieran).

Si está configurado como status check obligatorio, bloqueará el merge.

RepoGuardian no sustituye revisión humana ni pruebas en hardware.

---

## 10. Flujo de trabajo Git

- `main` debe estar estable.
- Ramas: `feature/*`, `fix/*`, `docs/*`, `refactor/*`, `test/*`, `chore/*`.
- Recomendado: Conventional Commits.

No se hace merge directo a `main`.

---

## 11. Restricciones específicas para agentes IA

- No refactorizar masivamente sin necesidad.
- No cambiar pinout o lógica de control sin documentarlo en `/docs`.
- No introducir cambios que puedan activar hardware de potencia sin una explicación clara.
- Priorizar cambios pequeños y revisables.
- Mantener el sistema en modo seguro ante fallos (failsafe).

El agente debe actuar con mentalidad de ingeniería: primero seguridad, luego funcionalidad.