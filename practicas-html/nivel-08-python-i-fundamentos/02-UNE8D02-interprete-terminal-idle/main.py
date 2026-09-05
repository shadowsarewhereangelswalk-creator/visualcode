import platform
import sys
from pathlib import Path


def obtener_entorno():
    return {
        "implementacion": platform.python_implementation(),
        "version": platform.python_version(),
        "ejecutable": sys.executable,
        "archivo": Path(__file__).name,
        "carpeta": str(Path(__file__).resolve().parent),
    }


def crear_ficha_servicio(nombre, precio, disponible):
    return {
        "nombre": nombre.strip().title(),
        "precio": float(precio),
        "disponible": bool(disponible),
    }


def mostrar_resultados():
    entorno = obtener_entorno()
    servicio = crear_ficha_servicio("automatización con python", 480, True)

    print("Entorno de ejecución")
    for clave, valor in entorno.items():
        print(f"{clave}: {valor}")

    print("\nServicio")
    for clave, valor in servicio.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    mostrar_resultados()
