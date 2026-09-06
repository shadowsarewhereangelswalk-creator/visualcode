import os
import platform
import sys
from pathlib import Path


def informacion_entorno():
    return {
        "python": platform.python_version(),
        "ejecutable": str(Path(sys.executable).resolve()),
        "prefijo": str(Path(sys.prefix).resolve()),
        "entorno_virtual": sys.prefix != sys.base_prefix,
        "plataforma": platform.system(),
        "modo": os.environ.get("APP_ENV", "development"),
    }


def validar_version(minima=(3, 12)):
    if sys.version_info < minima:
        raise RuntimeError(f"Se requiere Python {minima[0]}.{minima[1]} o superior")
    return True
