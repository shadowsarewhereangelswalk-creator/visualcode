import sys


PRACTICAS = (
    {"codigo": "P1", "dia": 8, "entrega": "Aplicación con templates y formularios"},
    {"codigo": "P2", "dia": 15, "entrega": "Persistencia y migraciones"},
    {"codigo": "P3", "dia": 22, "entrega": "API REST"},
    {"codigo": "P4", "dia": 26, "entrega": "Librería propia"},
    {"codigo": "P5", "dia": 30, "entrega": "Servicio web desplegable"},
)


if "--check" in sys.argv:
    assert len(PRACTICAS) == 5
    assert PRACTICAS[-1]["dia"] == 30
    print("UNE10D01 OK")
    raise SystemExit(0)


from flask import Flask, jsonify, render_template_string


app = Flask(__name__)


@app.get("/")
def inicio():
    return render_template_string(
        """
        <!doctype html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Nivel 10</title>
            <style>
                body { font-family: system-ui, sans-serif; margin: 0; background: whitesmoke; color: midnightblue; }
                main { max-width: 900px; margin: 48px auto; padding: 32px; background: white; border-radius: 18px; }
                li { margin: 12px 0; }
            </style>
        </head>
        <body>
            <main>
                <h1>Nivel 10 — Python III: Flask</h1>
                <p>Proyecto del nivel: Servicio Flask</p>
                <ol>
                    {% for practica in practicas %}
                    <li><strong>{{ practica.codigo }}</strong> · día {{ practica.dia }} · {{ practica.entrega }}</li>
                    {% endfor %}
                </ol>
            </main>
        </body>
        </html>
        """,
        practicas=PRACTICAS,
    )


@app.get("/api/plan")
def plan():
    return jsonify(nivel=10, clases=30, proyecto="Servicio Flask", practicas=PRACTICAS)


if __name__ == "__main__":
    app.run()
