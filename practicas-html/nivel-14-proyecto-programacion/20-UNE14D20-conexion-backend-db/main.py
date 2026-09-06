import sqlite3
conexion=sqlite3.connect("solicitudes.db")
conexion.execute("CREATE TABLE IF NOT EXISTS solicitudes(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,correo TEXT NOT NULL,mensaje TEXT NOT NULL,categoria TEXT NOT NULL,estado TEXT NOT NULL DEFAULT 'pendiente')")
conexion.commit(); print("Base de datos lista"); conexion.close()
