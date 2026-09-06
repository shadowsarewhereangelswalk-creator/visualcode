import sys
from datetime import datetime


MENSAJES = []


def validar_mensaje(nombre, correo, mensaje):
    errores = {}
    if len(nombre.strip()) < 2:
        errores["nombre"] = "Escribe un nombre válido."
    if "@" not in correo or "." not in correo.rsplit("@", 1)[-1]:
        errores["correo"] = "Escribe un correo válido."
    if len(mensaje.strip()) < 10:
        errores["mensaje"] = "El mensaje debe tener al menos 10 caracteres."
    return errores


if "--check" in sys.argv:
    assert not validar_mensaje("Karen", "karen@example.com", "Quiero información")
    assert set(validar_mensaje("", "correo", "hola")) == {"nombre", "correo", "mensaje"}
    print("UNE10D08 OK")
    raise SystemExit(0)


from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = "desarrollo-local-cambiar"


@app.route("/", methods=["GET", "POST"])
def contacto():
    datos = {"nombre": "", "correo": "", "mensaje": ""}
    errores = {}
    if request.method == "POST":
        datos = {campo: request.form.get(campo, "").strip() for campo in datos}
        errores = validar_mensaje(**datos)
        if not errores:
            MENSAJES.append({**datos, "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")})
            flash("Mensaje enviado correctamente.", "exito")
            return redirect(url_for("contacto"))
    return render_template("contacto.html", datos=datos, errores=errores)


@app.get("/mensajes")
def mensajes():
    return render_template("mensajes.html", mensajes=reversed(MENSAJES))


if __name__ == "__main__":
    app.run()
