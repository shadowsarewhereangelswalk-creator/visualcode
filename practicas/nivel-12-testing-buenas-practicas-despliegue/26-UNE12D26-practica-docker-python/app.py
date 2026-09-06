import os
import sys

PRACTICA = "UNE12D26"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D26"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from flask import Flask, jsonify, request


def create_app():
    application = Flask(__name__)
    tareas = []

    @application.get("/")
    def index():
        return jsonify(
            servicio="api-tareas",
            version=os.environ.get("APP_VERSION", "1.0.0"),
            endpoints=["/tareas", "/health"],
        )

    @application.get("/health")
    def health():
        return jsonify(status="ok", tareas=len(tareas))

    @application.get("/tareas")
    def listar_tareas():
        return jsonify(datos=tareas, total=len(tareas))

    @application.post("/tareas")
    def crear_tarea():
        datos = request.get_json(silent=True) or {}
        titulo = str(datos.get("titulo", "")).strip()
        if len(titulo) < 3:
            return jsonify(error="Título no válido"), 422
        tarea = {"id": len(tareas) + 1, "titulo": titulo, "completada": False}
        tareas.append(tarea)
        return jsonify(tarea), 201

    @application.patch("/tareas/<int:tarea_id>")
    def completar_tarea(tarea_id):
        tarea = next((item for item in tareas if item["id"] == tarea_id), None)
        if tarea is None:
            return jsonify(error="Tarea no encontrada"), 404
        tarea["completada"] = bool(
            (request.get_json(silent=True) or {}).get("completada")
        )
        return jsonify(tarea)

    return application


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000")),
        debug=False,
    )
