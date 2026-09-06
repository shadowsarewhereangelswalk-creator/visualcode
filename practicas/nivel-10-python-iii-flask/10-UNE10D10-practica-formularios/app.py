import sys


RESERVAS = []
SERVICIOS = {"mentoria": "Mentoría", "portafolio": "Revisión de portafolio", "entrevista": "Simulación de entrevista"}


def validar_reserva(datos):
    errores = {}
    if len(datos.get("nombre", "").strip()) < 2:
        errores["nombre"] = "Indica tu nombre."
    if "@" not in datos.get("correo", ""):
        errores["correo"] = "Indica un correo válido."
    if datos.get("servicio") not in SERVICIOS:
        errores["servicio"] = "Selecciona un servicio."
    if not datos.get("fecha"):
        errores["fecha"] = "Selecciona una fecha."
    if datos.get("modalidad") not in {"video", "presencial"}:
        errores["modalidad"] = "Selecciona una modalidad."
    return errores


if "--check" in sys.argv:
    datos = {"nombre": "Grace", "correo": "grace@example.com", "servicio": "mentoria", "fecha": "2027-04-10", "modalidad": "video"}
    assert not validar_reserva(datos)
    assert len(validar_reserva({})) == 5
    print("UNE10D10 OK")
    raise SystemExit(0)


from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = "reserva-local-cambiar"


@app.route("/", methods=["GET", "POST"])
def reservar():
    datos = request.form.to_dict() if request.method == "POST" else {}
    errores = validar_reserva(datos) if request.method == "POST" else {}
    if request.method == "POST" and not errores:
        RESERVAS.append({**datos, "servicio_nombre": SERVICIOS[datos["servicio"]]})
        flash("Reserva confirmada.")
        return redirect(url_for("confirmacion", indice=len(RESERVAS) - 1))
    return render_template("reserva.html", datos=datos, errores=errores, servicios=SERVICIOS)


@app.get("/confirmacion/<int:indice>")
def confirmacion(indice):
    if indice < 0 or indice >= len(RESERVAS):
        return redirect(url_for("reservar"))
    return render_template("confirmacion.html", reserva=RESERVAS[indice])


if __name__ == "__main__":
    app.run()
