from pathlib import Path
doc='''# Gestor de solicitudes\n\n## Instalación\nEjecuta `python main.py`.\n\n## Funciones\n- Registrar solicitudes.\n- Consultar solicitudes.\n- Clasificar mensajes.\n\n## Datos\nLa aplicación usa SQLite.\n'''
Path("MANUAL.md").write_text(doc,encoding="utf-8")
print("MANUAL.md creado")
