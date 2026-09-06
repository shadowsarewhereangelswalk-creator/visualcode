import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def inicio():
    return "UNE12D30 — aplicación preparada para despliegue"


@app.get("/salud")
def salud():
    return jsonify({"estado": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
