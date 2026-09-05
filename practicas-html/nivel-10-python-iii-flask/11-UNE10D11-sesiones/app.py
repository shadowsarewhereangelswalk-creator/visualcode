import os
import sys


def nombre_valido(nombre):
    return 2 <= len(nombre.strip()) <= 40


if "--check" in sys.argv:
    assert nombre_valido("Ada")
    assert not nombre_valido("A")
    print("UNE10D11 OK")
    raise SystemExit(0)


from flask import Flask, redirect, render_template_string, request, session, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "clave-solo-para-desarrollo")


PLANTILLA = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sesiones en Flask</title>
    <style>
        :root { font-family: system-ui, sans-serif; color: #312e81; background: #eef2ff; }
        main { width: min(650px, calc(100% - 40px)); margin: 60px auto; padding: 34px; border-radius: 20px; background: white; }
        form { display: flex; gap: 10px; flex-wrap: wrap; }
        input, button { padding: 11px; border-radius: 9px; font: inherit; }
        input { flex: 1; border: 1px solid #a5b4fc; }
        button, a { border: 0; background: #4f46e5; color: white; font-weight: 700; text-decoration: none; }
        button { cursor: pointer; }
        a { display: inline-block; padding: 10px 14px; border-radius: 9px; }
        .error { color: #b91c1c; }
    </style>
</head>
<body>
<main>
    <h1>Estado de la sesión</h1>
    <p>Visitas durante esta sesión: <strong>{{ visitas }}</strong></p>
    {% if usuario %}
    <h2>Hola, {{ usuario }}</h2>
    <p>Tu nombre y el contador se mantienen entre solicitudes.</p>
    <a href="{{ url_for('cerrar_sesion') }}">Cerrar sesión</a>
    {% else %}
    <form method="post">
        <input name="nombre" aria-label="Nombre" placeholder="Escribe tu nombre" required>
        <button type="submit">Guardar en sesión</button>
    </form>
    {% if error %}<p class="error">{{ error }}</p>{% endif %}
    {% endif %}
</main>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def inicio():
    session["visitas"] = session.get("visitas", 0) + 1
    error = ""
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        if nombre_valido(nombre):
            session["usuario"] = nombre
            return redirect(url_for("inicio"))
        error = "El nombre debe tener entre 2 y 40 caracteres."
    return render_template_string(PLANTILLA, usuario=session.get("usuario"), visitas=session["visitas"], error=error)


@app.get("/cerrar-sesion")
def cerrar_sesion():
    session.clear()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run()
