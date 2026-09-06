import os


def cargar_configuracion():
    puerto = int(os.environ.get("PORT", "8000"))
    if not 1 <= puerto <= 65535:
        raise ValueError("Puerto no válido")
    return {
        "entorno": os.environ.get("APP_ENV", "development"),
        "mensaje": os.environ.get("APP_MESSAGE", "Servicio disponible"),
        "puerto": puerto,
    }
