from pathlib import Path
from html.parser import HTMLParser
import ast
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PRACTICAS = ROOT / "practicas"
ERRORES = []
AVISOS = []

NIVELES = {
    3: ("nivel-03-html5-css3-ii", 30),
    4: ("nivel-04-javascript-i", 31),
    5: ("nivel-05-javascript-ii", 30),
    6: ("nivel-06-mysql", 31),
    7: ("nivel-07-postgresql", 31),
    8: ("nivel-08-python-i-fundamentos", 28),
    9: ("nivel-09-python-ii-tkinter", 31),
    10: ("nivel-10-python-iii-flask", 30),
    11: ("nivel-11-python-iv-django", 31),
    12: ("nivel-12-testing-buenas-practicas-despliegue", 30),
    13: ("nivel-13-ia-para-programadores", 31),
    14: ("nivel-14-proyecto-programacion", 31),
}

PRACTICAS_N2 = {
    "01-etiquetas-basicas": "UNE2D09",
    "02-listas-enlaces-multimedia": "UNE2D13",
    "03-formulario-contacto": "UNE2D22",
    "04-hoja-estilos-css3": "UNE2D28",
    "05-landing-page-final": "UNE2D31",
}

class ReferenciasHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.referencias = []

    def handle_starttag(self, tag, attrs):
        for clave, valor in attrs:
            if clave in {"href", "src"} and valor:
                self.referencias.append(valor)


def error(mensaje):
    ERRORES.append(mensaje)


def aviso(mensaje):
    AVISOS.append(mensaje)


def es_externa(valor):
    valor = valor.strip()
    return not valor or valor.startswith(("/", "http://", "https://", "mailto:", "tel:", "data:", "#", "javascript:", "{{", "{%"))


def limpiar_destino(destino):
    destino = destino.strip().strip("<>")
    destino = destino.split("#", 1)[0].split("?", 1)[0]
    return destino


def validar_markdown(ruta):
    texto = ruta.read_text(encoding="utf-8")
    for destino in re.findall(r"\[[^\]]*\]\(([^)]+)\)", texto):
        destino = limpiar_destino(destino)
        if es_externa(destino):
            continue
        objetivo = (ruta.parent / destino).resolve()
        if not objetivo.exists():
            error(f"Enlace Markdown roto: {ruta.relative_to(ROOT)} -> {destino}")


def validar_html(ruta):
    texto = ruta.read_text(encoding="utf-8")
    parser = ReferenciasHTML()
    try:
        parser.feed(texto)
    except Exception as exc:
        error(f"HTML no parseable: {ruta.relative_to(ROOT)}: {exc}")
        return
    for destino in parser.referencias:
        destino = limpiar_destino(destino)
        if es_externa(destino):
            continue
        if "${" in destino or "{{" in destino or "{%" in destino:
            continue
        objetivo = (ruta.parent / destino).resolve()
        if not objetivo.exists():
            error(f"Referencia HTML local rota: {ruta.relative_to(ROOT)} -> {destino}")


def validar_python(ruta):
    try:
        ast.parse(ruta.read_text(encoding="utf-8"), filename=str(ruta))
    except SyntaxError as exc:
        error(f"Python inválido: {ruta.relative_to(ROOT)}:{exc.lineno}: {exc.msg}")


def validar_javascript(ruta):
    proceso = subprocess.run(["node", "--check", str(ruta)], capture_output=True, text=True)
    if proceso.returncode != 0:
        detalle = (proceso.stderr or proceso.stdout).strip().replace("\n", " ")
        error(f"JavaScript inválido: {ruta.relative_to(ROOT)}: {detalle}")


def validar_json(ruta):
    try:
        json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        error(f"JSON inválido: {ruta.relative_to(ROOT)}:{exc.lineno}: {exc.msg}")


def validar_nivel_2():
    for carpeta, identificador in PRACTICAS_N2.items():
        ruta = PRACTICAS / carpeta
        if not ruta.is_dir():
            error(f"Falta práctica de Nivel 2: {carpeta}")
            continue
        readme = ruta / "README.md"
        if not readme.exists():
            error(f"Falta README: {ruta.relative_to(ROOT)}")
        elif identificador not in readme.read_text(encoding="utf-8"):
            error(f"README de {carpeta} no declara {identificador}")
        fuentes = [p for p in ruta.rglob("*") if p.is_file() and p.name.lower() != "readme.md"]
        if not fuentes:
            error(f"Práctica sin archivos fuente: {ruta.relative_to(ROOT)}")


def validar_niveles():
    for nivel, (nombre, cantidad) in NIVELES.items():
        ruta = PRACTICAS / nombre
        if not ruta.is_dir():
            error(f"Falta carpeta del Nivel {nivel}: {nombre}")
            continue
        if not (ruta / "README.md").exists():
            error(f"Falta README del Nivel {nivel}")
        carpetas = [p for p in ruta.iterdir() if p.is_dir()]
        encontrados = {}
        patron = re.compile(rf"UNE{nivel}D(\d{{2}})")
        for carpeta in carpetas:
            coincidencia = patron.search(carpeta.name)
            if not coincidencia:
                aviso(f"Carpeta sin ID UNE en Nivel {nivel}: {carpeta.name}")
                continue
            identificador = f"UNE{nivel}D{coincidencia.group(1)}"
            if identificador in encontrados:
                error(f"ID duplicado {identificador}: {encontrados[identificador].name} y {carpeta.name}")
            encontrados[identificador] = carpeta
            fuentes = [p for p in carpeta.rglob("*") if p.is_file() and p.name.lower() != "readme.md"]
            if not fuentes:
                error(f"Clase sin archivos fuente: {carpeta.relative_to(ROOT)}")
        esperados = {f"UNE{nivel}D{i:02d}" for i in range(1, cantidad + 1)}
        faltantes = sorted(esperados - set(encontrados))
        extras = sorted(set(encontrados) - esperados)
        if faltantes:
            error(f"Nivel {nivel}: faltan IDs {', '.join(faltantes)}")
        if extras:
            error(f"Nivel {nivel}: IDs fuera de rango {', '.join(extras)}")
        if len(encontrados) != cantidad:
            error(f"Nivel {nivel}: se esperaban {cantidad} clases y hay {len(encontrados)} IDs válidos")


def validar_archivos():
    for ruta in ROOT.rglob("*"):
        if not ruta.is_file() or ".git" in ruta.parts:
            continue
        if ruta.stat().st_size == 0:
            error(f"Archivo vacío: {ruta.relative_to(ROOT)}")
        sufijo = ruta.suffix.lower()
        if sufijo == ".md":
            validar_markdown(ruta)
        elif sufijo == ".html":
            validar_html(ruta)
        elif sufijo == ".py":
            validar_python(ruta)
        elif sufijo == ".js":
            validar_javascript(ruta)
        elif sufijo == ".json":
            validar_json(ruta)


def validar_raiz():
    if (ROOT / "practicas-html").exists():
        error("La carpeta eliminada practicas-html volvió a aparecer")
    if not (ROOT / "README.md").exists():
        error("Falta README.md en la raíz")
    if not PRACTICAS.is_dir():
        error("Falta la carpeta oficial practicas/")


def main():
    validar_raiz()
    validar_nivel_2()
    validar_niveles()
    validar_archivos()
    resultado = {"errores": len(ERRORES), "avisos": len(AVISOS), "detalle_errores": ERRORES, "detalle_avisos": AVISOS}
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 1 if ERRORES else 0


if __name__ == "__main__":
    sys.exit(main())
