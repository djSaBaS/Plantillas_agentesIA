# Importamos argparse para leer argumentos de ejecución
import argparse
# Importamos os para validar rutas y existencia de archivos
import os
# Importamos subprocess para ejecutar git diff
import subprocess
# Importamos sys para devolver códigos de salida consistentes
import sys
# Importamos List para tipar colecciones
from typing import List, Tuple


# Ejecutamos un comando y devolvemos stdout como texto
def run_cmd(cmd: List[str]) -> str:
    # Ejecutamos el comando capturando salida
    completed = subprocess.run(cmd, capture_output=True, text=True)
    # Si el comando falla, devolvemos error claro
    if completed.returncode != 0:
        # Escribimos stderr para diagnóstico
        sys.stderr.write(completed.stderr + "\n")
        # Lanzamos excepción controlada
        raise RuntimeError("No se pudo ejecutar un comando requerido.")
    # Devolvemos stdout
    return completed.stdout


# Obtenemos una lista de rutas cambiadas en el PR
def get_changed_paths(base_ref: str, head_ref: str) -> List[Tuple[str, str]]:
    # Pedimos a git estados y rutas
    out = run_cmd(["git", "diff", "--name-status", f"{base_ref}...{head_ref}"])
    # Inicializamos lista
    items: List[Tuple[str, str]] = []
    # Recorremos líneas
    for line in out.splitlines():
        # Saltamos vacíos
        if not line.strip():
            continue
        # Separamos estado y ruta
        parts = line.split("\t", 1)
        # Guardamos estado y ruta
        items.append((parts[0].strip(), parts[1].strip()))
    # Devolvemos cambios
    return items


# Construimos un bloque Markdown
def md_section(title: str, ok: bool, details: List[str]) -> str:
    # Elegimos icono según estado
    icon = "✅" if ok else "❌"
    # Iniciamos sección
    lines = [f"### {icon} {title}"]
    # Añadimos detalles
    lines.extend([f"- {d}" for d in details])
    # Línea en blanco
    lines.append("")
    # Devolvemos markdown
    return "\n".join(lines)


# Punto de entrada del script
def main() -> int:
    # Definimos parser
    parser = argparse.ArgumentParser()
    # Añadimos argumentos
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--head-ref", required=True)
    parser.add_argument("--report-path", required=True)
    # Parseamos
    args = parser.parse_args()

    # Leemos cambios
    changes = get_changed_paths(args.base_ref, args.head_ref)

    # Preparamos secciones y estado global
    sections: List[str] = []
    overall_ok = True

    # Regla 1: no subir .env
    env_hits = [p for s, p in changes if p == ".env" or p.endswith("/.env")]
    rule_ok = len(env_hits) == 0
    overall_ok = overall_ok and rule_ok
    sections.append(md_section(
        "No se suben secretos (.env)",
        rule_ok,
        ["No se detectó `.env` ✅"] if rule_ok else ["Se detectó `.env` en el PR. Elimina el archivo y usa `.env.example`."]
    ))

    # Regla 2: si se cambia src/, también debe cambiar tests/
    src_changed = any(p.startswith("src/") and s in ("A", "M", "R") for s, p in changes)
    tests_changed = any(p.startswith("tests/") and s in ("A", "M", "R") for s, p in changes)
    rule_ok = (not src_changed) or tests_changed
    overall_ok = overall_ok and rule_ok
    sections.append(md_section(
        "Tests asociados a cambios en src",
        rule_ok,
        ["No se detectaron cambios en `src/`."] if not src_changed else (
            ["Se detectaron cambios en `tests/` ✅"] if tests_changed else ["Cambiaste `src/` pero no `tests/`. Añade/actualiza tests."]
        )
    ))

    # Regla 3: si hay cambios de código, version.md debe cambiar
    code_changed = any(p.startswith(("src/", "public/", "scripts/")) and s in ("A", "M", "R") for s, p in changes)
    version_touched = any(p == "version.md" and s in ("A", "M") for s, p in changes)
    rule_ok = (not code_changed) or version_touched
    overall_ok = overall_ok and rule_ok
    sections.append(md_section(
        "version.md actualizado cuando cambia código",
        rule_ok,
        ["No se detectaron cambios de código."] if not code_changed else (
            ["Se detectó actualización de `version.md` ✅"] if version_touched else ["Cambiaste código pero no `version.md`. Añade una entrada."]
        )
    ))

    # Regla 4: si se tocan carpetas de primer nivel, su info.md debe tocarse
    touched = set()
    for _, p in changes:
        if "/" in p:
            top = p.split("/", 1)[0]
            if top not in {".git", ".github", "vendor", "venv", "__pycache__", "node_modules", "reports", "dist", "build"}:
                touched.add(top)
    missing = []
    for d in sorted(touched):
        info_path = f"{d}/info.md"
        info_touched = any(p == info_path and s in ("A", "M", "R") for s, p in changes)
        if not info_touched and os.path.isfile(info_path):
            missing.append(info_path)
    rule_ok = len(missing) == 0
    overall_ok = overall_ok and rule_ok
    sections.append(md_section(
        "info.md actualizado cuando cambia la carpeta",
        rule_ok,
        ["No se detectaron carpetas afectadas."] if not touched else (
            ["info.md actualizado en carpetas afectadas ✅"] if rule_ok else [f"Falta actualizar: `{m}`" for m in missing]
        )
    ))

    # Cabecera del reporte
    status = "✅ APROBADO" if overall_ok else "❌ BLOQUEADO"
    report = []
    report.append(f"## 🛡 RepoGuardian — Informe de Cumplimiento ({status})")
    report.append("")
    report.append("Este informe valida reglas básicas del repositorio (seguridad, documentación y disciplina de pruebas).")
    report.append("")
    report.extend(sections)
    report.append("**Resultado:** " + ("El PR cumple las reglas." if overall_ok else "El PR queda bloqueado. Corrige los ❌ y vuelve a hacer push."))
    report.append("")

    # Creamos carpeta destino
    os.makedirs(os.path.dirname(args.report_path), exist_ok=True)
    # Escribimos reporte
    with open(args.report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    # Devolvemos código
    return 0 if overall_ok else 2


# Ejecutamos la función principal
if __name__ == "__main__":
    raise SystemExit(main())
