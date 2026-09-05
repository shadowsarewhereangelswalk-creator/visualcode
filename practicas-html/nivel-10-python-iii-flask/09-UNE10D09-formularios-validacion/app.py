import re
import sys


PATRON_CORREO = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def validar_registro(datos):
    errores = {}
    nombre = datos.get("nombre", "").strip()
    correo = datos.get("correo", "").strip().lower()
    clave = datos.get("clave", "")
    confirmacion = datos.get("confirmacion", "")
    if len(nombre) < 2:
        errores["nombre"] = "El nombre debe tener al menos 2 caracteres."
    if not PATRON_CORREO.fullmatch(correo):
        errores["correo"] = "El correo no tiene un formato válido."
    if len(clave) < 8 or not any(caracter.isdigit() for caracter in clave):
        errores["clave"] = "La clave debe tener 8 caracteres e incluir un número."
    if not confirmacion or confirmacion != clave:
        errores["confirmacion"] = "Las claves no coinciden."
    if datos.get("terminos") != "acepto":
        errores["terminos"] = "Debes aceptar los términos."
    return errores


if "--check" in sys.argv:
    validos = {"nombre": "Ada", "correo": "ada@example.com", "clave": "codigo123", "confirmacion": "codigo123", "terminos": "acepto"}
    assert not validar_registro(validos)
    assert len(validar_registro({})) == 5
    print("UNE10D09 OK")
    raise SystemExit(0)


from flask import Flask, render_template_string, request


app = Flask(__name__)


PLANTILLA = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Crear cuenta</title>
    <style>
        :root { font-family: system-ui, sans-serif; color: #1e1b4b; background: #eef2ff; }
        main { width: min(520px, calc(100% - 40px)); margin: 48px auto; padding: 32px; box-sizing: border-box; background: white; border-radius: 20px; }
        form { display: grid; gap: 9px; }
        label { margin-top: 8px; font-weight: 700; }
        input { padding: 11px; border: 1px solid #c7d2fe; border-radius: 9px; font: inherit; }
        small { color: #b91c1c; }
        button { margin-top: 12px; padding: 12px; border: 0; border-radius: 9px; background: #4338ca; color: white; font: inherit; font-weight: 700; }
        .terminos { display: flex; gap: 8px; align-items: center; font-weight: 400; }
        .exito { padding: 14px; color: #14532d; background: #dcfce7; border-radius: 10px; }
    </style>
</head>
<body>
<main>
    <h1>Crear cuenta</h1>
    {% if registrado %}<p class="exito">Cuenta creada para {{ datos.nombre }}.</p>{% endif %}
    <form method="post" novalidate>
        <label for="nombre">Nombre</label>
        <input id="nombre" name="nombre" value="{{ datos.get('nombre', '') }}">
        {% if errores.nombre %}<small>{{ errores.nombre }}</small>{% endif %}
        <label for="correo">Correo</label>
        <input id="correo" name="correo" type="email" value="{{ datos.get('correo', '') }}">
        {% if errores.correo %}<small>{{ errores.correo }}</small>{% endif %}
        <label for="clave">Clave</label>
        <input id="clave" name="clave" type="password">
        {% if errores.clave %}<small>{{ errores.clave }}</small>{% endif %}
        <label for="confirmacion">Confirmar clave</label>
        <input id="confirmacion" name="confirmacion" type="password">
        {% if errores.confirmacion %}<small>{{ errores.confirmacion }}</small>{% endif %}
        <label class="terminos"><input name="terminos" type="checkbox" value="acepto"> Acepto los términos</label>
        {% if errores.terminos %}<small>{{ errores.terminos }}</small>{% endif %}
        <button type="submit">Registrarme</button>
    </form>
</main>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def registro():
    datos = request.form.to_dict() if request.method == "POST" else {}
    errores = validar_registro(datos) if request.method == "POST" else {}
    return render_template_string(PLANTILLA, datos=datos, errores=errores, registrado=request.method == "POST" and not errores)


if __name__ == "__main__":
    app.run()
