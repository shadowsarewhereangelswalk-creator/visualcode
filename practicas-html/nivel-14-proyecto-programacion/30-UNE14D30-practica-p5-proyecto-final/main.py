import sqlite3,json,re
def categoria(texto):
    t=texto.lower()
    if any(p in t for p in ("error","problema","no funciona")): return "soporte"
    if any(p in t for p in ("precio","comprar","cotización")): return "ventas"
    return "general"
def crear(con,nombre,correo,mensaje):
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}",correo) is None: raise ValueError("Correo inválido")
    cat=categoria(mensaje);cur=con.execute("INSERT INTO solicitudes(nombre,correo,mensaje,categoria) VALUES(?,?,?,?)",(nombre,correo,mensaje,cat));con.commit();return cur.lastrowid
con=sqlite3.connect("proyecto_final.db");con.row_factory=sqlite3.Row;con.execute("CREATE TABLE IF NOT EXISTS solicitudes(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,correo TEXT NOT NULL,mensaje TEXT NOT NULL,categoria TEXT NOT NULL)");crear(con,"Karen","karen@ejemplo.com","Necesito precio del servicio");print(json.dumps([dict(f) for f in con.execute("SELECT * FROM solicitudes")],ensure_ascii=False,indent=2));con.close()
