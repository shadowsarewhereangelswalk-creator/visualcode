import sqlite3
def guardar(con,nombre,mensaje):
    cur=con.execute("INSERT INTO solicitudes(nombre,mensaje) VALUES(?,?)",(nombre,mensaje));con.commit();return cur.lastrowid
con=sqlite3.connect(":memory:");con.execute("CREATE TABLE solicitudes(id INTEGER PRIMARY KEY,nombre TEXT,mensaje TEXT)");id_=guardar(con,"Karen","Prueba de integración");fila=con.execute("SELECT nombre,mensaje FROM solicitudes WHERE id=?",(id_,)).fetchone();assert fila==("Karen","Prueba de integración");print("Integración OK")
