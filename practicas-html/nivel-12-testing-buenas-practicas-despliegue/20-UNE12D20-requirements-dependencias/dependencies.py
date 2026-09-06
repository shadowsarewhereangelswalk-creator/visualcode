from pathlib import Path

from packaging.requirements import Requirement


def leer_dependencias(ruta):
    dependencias = []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        valor = linea.strip()
        if valor and not valor.startswith("-r "):
            dependencias.append(Requirement(valor))
    return dependencias


def crear_informe(dependencias):
    return [
        {
            "nombre": dependencia.name,
            "version": str(dependencia.specifier),
            "extras": sorted(dependencia.extras),
        }
        for dependencia in sorted(dependencias, key=lambda item: item.name.casefold())
    ]
