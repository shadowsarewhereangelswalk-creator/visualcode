import sqlite3,json
def conectar():
    con=sqlite3.connect("solicitudes.db");con.row_factory=sqlite3.Row;con.execute("CREATE TABLE IF NOT EXISTS solicitudes(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,correo TEXT NOT NULL,mensaje TEXT NOT NULL,categoria TEXT NOT NULL)");return con
def crear(nombre,correo,mensaje,categoria="general"):
    con=conectar();cur=con.execute("INSERT INTO solicitudes(nombre,correo,mensaje,categoria) VALUES(?,?,?,?)",(nombre,correo,mensaje,categoria));con.commit();id_=cur.lastrowid;con.close();return id_
def listar():
    con=conectar();datos=[dict(f) for f in con.execute("SELECT * FROM solicitudes ORDER BY id DESC")];con.close();return datos
crear("Karen","karen@ejemplo.com","Necesito soporte","soporte");print(json.dumps(listar(),ensure_ascii=False,indent=2))
