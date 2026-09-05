import sys


PROYECTOS = (
    {"nombre": "Panel de ventas", "categoria": "Datos", "avance": 92, "activo": True},
    {"nombre": "Asistente interno", "categoria": "IA", "avance": 68, "activo": True},
    {"nombre": "Portal de clientes", "categoria": "Web", "avance": 100, "activo": False},
)


def porcentaje(valor):
    return f"{valor}%"


if "--check" in sys.argv:
    assert porcentaje(75) == "75%"
    assert len([proyecto for proyecto in PROYECTOS if proyecto["activo"]]) == 2
    print("UNE10D07 OK")
    raise SystemExit(0)


from flask import Flask, render_template


app = Flask(__name__)
app.jinja_env.filters["porcentaje"] = porcentaje


@app.get("/")
def tablero():
    resumen = {
        "total": len(PROYECTOS),
        "activos": sum(proyecto["activo"] for proyecto in PROYECTOS),
        "promedio": round(sum(proyecto["avance"] for proyecto in PROYECTOS) / len(PROYECTOS)),
    }
    return render_template("tablero.html", proyectos=PROYECTOS, resumen=resumen)


if __name__ == "__main__":
    app.run()
