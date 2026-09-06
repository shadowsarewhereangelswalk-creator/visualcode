import json
import os
import re
import sqlite3
import urllib.error
import urllib.request
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
DB_PATH = os.getenv("DB_PATH", "proyecto_final.db")
CATEGORIAS = {"soporte", "ventas", "general"}

PAGINA = """
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Clasificador inteligente</title>
<style>
body{font-family:Arial,sans-serif;max-width:900px;margin:40px auto;padding:0 20px;background:#f5f7fb;color:#172033}main{background:white;padding:24px;border-radius:16px;box-shadow:0 8px 30px #0001}form{display:grid;gap:12px}input,textarea,button{font:inherit;padding:12px;border:1px solid #ccd3df;border-radius:10px}button{background:#172033;color:white;cursor:pointer}table{width:100%;border-collapse:collapse;margin-top:24px}th,td{text-align:left;padding:10px;border-bottom:1px solid #e5e8ef}.estado{margin-top:12px;min-height:24px}
</style>
</head>
<body>
<main>
<h1>Clasificador inteligente de solicitudes</h1>
<form id="formulario">
<input id="nombre" placeholder="Nombre" required>
<input id="correo" type="email" placeholder="Correo" required>
<textarea id="mensaje" placeholder="Mensaje" required></textarea>
<button>Guardar y clasificar</button>
</form>
<div class="estado" id="estado"></div>
<table>
<thead><tr><th>ID</th><th>Nombre</th><th>Categoría</th><th>Fuente</th></tr></thead>
<tbody id="filas"></tbody>
</table>
</main>
<script>
function celda(texto){const td=document.createElement('td');td.textContent=String(texto);return td}
async function cargar(){const r=await fetch('/api/solicitudes');const datos=await r.json();const filasNuevas=datos.map(x=>{const tr=document.createElement('tr');tr.append(celda(x.id),celda(x.nombre),celda(x.categoria),celda(x.fuente));return tr});filas.replaceChildren(...filasNuevas)}
formulario.addEventListener('submit',async e=>{e.preventDefault();estado.textContent='Procesando...';const r=await fetch('/api/solicitudes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({nombre:nombre.value,correo:correo.value,mensaje:mensaje.value})});const d=await r.json();estado.textContent=r.ok?`Guardado como ${d.categoria} (${d.fuente})`:d.error;if(r.ok){formulario.reset();cargar()}})
cargar()
</script>
</body>
</html>
"""


def conectar():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


def inicializar():
    with conectar() as conexion:
        conexion.execute(
            "CREATE TABLE IF NOT EXISTS solicitudes(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,correo TEXT NOT NULL,mensaje TEXT NOT NULL,categoria TEXT NOT NULL,fuente TEXT NOT NULL,creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)"
        )


def validar_correo(correo):
    correo = correo.strip().lower()
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("Correo inválido")
    return correo


def clasificar_local(mensaje):
    contenido = mensaje.lower()
    if any(palabra in contenido for palabra in ("error", "problema", "no funciona", "fallo")):
        return "soporte"
    if any(palabra in contenido for palabra in ("precio", "comprar", "cotización", "contratar")):
        return "ventas"
    return "general"


def clasificar_ia(mensaje):
    url = os.getenv("AI_API_URL", "").strip()
    clave = os.getenv("AI_API_KEY", "").strip()
    modelo = os.getenv("AI_MODEL", "").strip()
    if not url or not clave or not modelo:
        return clasificar_local(mensaje), "local"
    cuerpo = json.dumps({
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Clasifica el mensaje como soporte, ventas o general. Responde únicamente con una de esas palabras."},
            {"role": "user", "content": mensaje},
        ],
    }).encode("utf-8")
    solicitud = urllib.request.Request(
        url,
        data=cuerpo,
        headers={"Authorization": f"Bearer {clave}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(solicitud, timeout=30) as respuesta:
            salida = json.loads(respuesta.read().decode("utf-8"))
        categoria = salida["choices"][0]["message"]["content"].strip().lower()
        if categoria not in CATEGORIAS:
            raise ValueError("Categoría inesperada")
        return categoria, "ia"
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
        return clasificar_local(mensaje), "local-respaldo"


@app.get("/")
def inicio():
    return render_template_string(PAGINA)


@app.get("/api/solicitudes")
def listar_solicitudes():
    with conectar() as conexion:
        filas = conexion.execute(
            "SELECT id,nombre,correo,mensaje,categoria,fuente,creado_en FROM solicitudes ORDER BY id DESC"
        ).fetchall()
    return jsonify([dict(fila) for fila in filas])


@app.post("/api/solicitudes")
def crear_solicitud():
    datos = request.get_json(silent=True) or {}
    nombre = " ".join(str(datos.get("nombre", "")).split())
    mensaje = str(datos.get("mensaje", "")).strip()
    try:
        correo = validar_correo(str(datos.get("correo", "")))
        if len(nombre) < 2:
            raise ValueError("Nombre inválido")
        if len(mensaje) < 5:
            raise ValueError("Mensaje demasiado corto")
        categoria, fuente = clasificar_ia(mensaje)
        with conectar() as conexion:
            cursor = conexion.execute(
                "INSERT INTO solicitudes(nombre,correo,mensaje,categoria,fuente) VALUES(?,?,?,?,?)",
                (nombre, correo, mensaje, categoria, fuente),
            )
            identificador = cursor.lastrowid
        return jsonify({"id": identificador, "categoria": categoria, "fuente": fuente}), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.get("/salud")
def salud():
    return jsonify({"estado": "ok"})


inicializar()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
