from pathlib import Path
requisitos='''# Requerimientos\n\nRF01 Crear solicitudes.\nRF02 Listar solicitudes.\nRF03 Clasificar mensajes.\nRNF01 Validar entradas.\n'''
sql='''CREATE TABLE solicitudes (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,correo TEXT NOT NULL,mensaje TEXT NOT NULL,categoria TEXT NOT NULL,estado TEXT NOT NULL DEFAULT 'pendiente');\n'''
Path("REQUERIMIENTOS.md").write_text(requisitos,encoding="utf-8")
Path("schema.sql").write_text(sql,encoding="utf-8")
print("REQUERIMIENTOS.md y schema.sql creados")
