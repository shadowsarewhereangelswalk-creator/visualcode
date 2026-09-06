import importlib.metadata
import sys
from pathlib import Path


def diagnosticar(paquetes):
    instalados = {}
    faltantes = []
    for paquete in paquetes:
        try:
            instalados[paquete] = importlib.metadata.version(paquete)
        except importlib.metadata.PackageNotFoundError:
            faltantes.append(paquete)
    return {
        "entorno_virtual": sys.prefix != sys.base_prefix,
        "ejecutable": str(Path(sys.executable).resolve()),
        "instalados": instalados,
        "faltantes": faltantes,
        "listo": sys.prefix != sys.base_prefix and not faltantes,
    }
