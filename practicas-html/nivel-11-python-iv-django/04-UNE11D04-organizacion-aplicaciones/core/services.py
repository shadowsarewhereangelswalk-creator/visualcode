SECCIONES = (
    {"nombre": "Inicio", "ruta": "/"},
    {"nombre": "Catálogo", "ruta": "/catalogo/"},
)


def mapa_aplicacion():
    return {"proyecto": "portal", "aplicaciones": ["core", "catalogo"], "secciones": SECCIONES}

