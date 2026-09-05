import sys


COLORES = {"azul": "#1d4ed8", "verde": "#15803d", "violeta": "#7e22ce"}


def color_permitido(color):
    return color if color in COLORES else "azul"


if "--check" in sys.argv:
    assert color_permitido("verde") == "verde"
    assert color_permitido("rojo") == "azul"
    print("UNE10D13 OK")
    raise SystemExit(0)


from flask import Flask, make_response, redirect, render_template_string, request, url_for


app = Flask(__name__)


PLANTILLA = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Cookies en Flask</title>
    <style>
        :root { font-family: system-ui, sans-serif; background: #f8fafc; }
        main { width: min(620px, calc(100% - 40px)); margin: 60px auto; padding: 34px; border-top: 8px solid {{ codigo_color }}; border-radius: 18px; background: white; box-shadow: 0 18px 44px #0f172a1a; }
        form { display: flex; gap: 10px; flex-wrap: wrap; }
        select, button, a { padding: 10px 14px; border-radius: 9px; font: inherit; }
        button { border: 0; color: white; background: {{ codigo_color }}; font-weight: 700; }
        a { color: {{ codigo_color }}; }
    </style>
</head>
<body>
<main>
    <h1>Preferencia guardada en una cookie</h1>
    <p>Color actual: <strong>{{ color }}</strong></p>
    <p>La cookie permanece en el navegador durante 30 días.</p>
    <form method="post">
        <select name="color" aria-label="Color">
            {% for opcion in colores %}<option value="{{ opcion }}" {% if opcion == color %}selected{% endif %}>{{ opcion|capitalize }}</option>{% endfor %}
        </select>
        <button type="submit">Guardar preferencia</button>
    </form>
    <p><a href="{{ url_for('eliminar') }}">Eliminar cookie</a></p>
</main>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        color = color_permitido(request.form.get("color", ""))
        respuesta = make_response(redirect(url_for("inicio")))
        respuesta.set_cookie("color_preferido", color, max_age=60 * 60 * 24 * 30, httponly=True, samesite="Lax")
        return respuesta
    color = color_permitido(request.cookies.get("color_preferido", "azul"))
    return render_template_string(PLANTILLA, color=color, codigo_color=COLORES[color], colores=COLORES)


@app.get("/eliminar")
def eliminar():
    respuesta = make_response(redirect(url_for("inicio")))
    respuesta.delete_cookie("color_preferido")
    return respuesta


if __name__ == "__main__":
    app.run()
