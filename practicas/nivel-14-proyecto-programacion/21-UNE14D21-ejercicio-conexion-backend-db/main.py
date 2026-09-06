import sqlite3
con=sqlite3.connect(":memory:")
con.execute("CREATE TABLE solicitudes(id INTEGER PRIMARY KEY,nombre TEXT,mensaje TEXT)")
con.execute("INSERT INTO solicitudes(nombre,mensaje) VALUES(?,?)",("Karen","Necesito soporte"))
for fila in con.execute("SELECT id,nombre,mensaje FROM solicitudes"): print(fila)
con.close()
