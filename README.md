# 🧠 Plantillas Profesionales de Proyecto (PHP · Python · Arduino)

Este repositorio contiene tres plantillas base listas para usar: `PHP/`, `Python/` y `Arduino/`.

Cada carpeta es un proyecto independiente con estructura y CI. Copia una carpeta completa a un repo nuevo y tendrás:
- documentación viva (info.md por carpeta)
- control de cambios (version.md)
- tests (cuando aplique)
- GitHub Actions
- RepoGuardian

## 🛡 RepoGuardian (cómo funciona)

RepoGuardian se ejecuta en Pull Requests y genera un informe en:
- el propio PR (comentario),
- el “Step Summary” del workflow,
- y como artefacto.

Además, si lo configuras como “status check” obligatorio en la rama, **bloquea el merge**.

Reglas principales:
- No se puede subir `.env`.
- Si cambias `src/`, debes cambiar `tests/`.
- Si cambias código, debes actualizar `version.md`.
- Si cambias contenido dentro de una carpeta de primer nivel, debes actualizar su `info.md`.

## ✅ Activar el bloqueo del merge

GitHub → `Settings` → `Branches` → `Branch protection rules`:
- Require a pull request before merging
- Require status checks to pass before merging
- Selecciona: `RepoGuardian - Cumplimiento agent.md`
