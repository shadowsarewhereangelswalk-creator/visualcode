import os
import sys


PRODUCTOS = {
    "curso-html": {"nombre": "Curso HTML", "precio": 29},
    "curso-python": {"nombre": "Curso Python", "precio": 49},
    "curso-flask": {"nombre": "Curso Flask", "precio": 59},
}


def resumir_carrito(cantidades):
    lineas = []
    for codigo, cantidad in cantidades.items():
        if codigo in PRODUCTOS and cantidad > 0:
            producto = PRODUCTOS[codigo]
            lineas.append({"codigo": codigo, **producto, "cantidad": cantidad, "subtotal": producto["precio"] * cantidad})
    return lineas, sum(linea["subtotal"] for linea in lineas)


if "--check" in sys.argv:
    lineas, total = resumir_carrito({"curso-html": 2, "curso-flask": 1})
    assert len(lineas) == 2
    assert total == 117
    print("UNE10D12 OK")
    raise SystemExit(0)


from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "carrito-solo-desarrollo")


@app.get("/")
def catalogo():
    cantidades = session.get("carrito", {})
    unidades = sum(cantidades.values())
    return render_template("catalogo.html", productos=PRODUCTOS, unidades=unidades)


@app.post("/carrito/agregar/<codigo>")
def agregar(codigo):
    if codigo in PRODUCTOS:
        carrito = session.get("carrito", {})
        carrito[codigo] = min(carrito.get(codigo, 0) + 1, 9)
        session["carrito"] = carrito
    return redirect(request.referrer or url_for("catalogo"))


@app.get("/carrito")
def carrito():
    lineas, total = resumir_carrito(session.get("carrito", {}))
    return render_template("carrito.html", lineas=lineas, total=total)


@app.post("/carrito/actualizar/<codigo>")
def actualizar(codigo):
    carrito = session.get("carrito", {})
    cantidad = request.form.get("cantidad", type=int)
    if codigo in carrito and cantidad is not None:
        if cantidad <= 0:
            carrito.pop(codigo)
        else:
            carrito[codigo] = min(cantidad, 9)
        session["carrito"] = carrito
    return redirect(url_for("carrito"))


@app.post("/carrito/vaciar")
def vaciar():
    session.pop("carrito", None)
    return redirect(url_for("carrito"))


if __name__ == "__main__":
    app.run()
