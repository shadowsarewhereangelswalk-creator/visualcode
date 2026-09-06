from pathlib import Path
html='''<!doctype html><html lang="es"><meta charset="utf-8"><title>Panel</title><body><header><h1>Panel de solicitudes</h1></header><main><section><h2>Pendientes</h2><article><strong>Soporte</strong><p>Mi cuenta no funciona</p></article></section></main></body></html>'''
Path("panel.html").write_text(html,encoding="utf-8")
print("panel.html creado")
