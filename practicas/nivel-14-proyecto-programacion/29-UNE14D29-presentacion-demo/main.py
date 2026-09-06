import json
import os

presentacion = {
    "titulo": "Demo final — Clasificador inteligente de solicitudes",
    "duracion_objetivo_minutos": 5,
    "url_demo": os.getenv("APP_URL", "http://127.0.0.1:5000"),
    "secuencia": [
        {"paso": 1, "tema": "Problema", "mensaje": "Las solicitudes llegan sin clasificar y retrasan la atención."},
        {"paso": 2, "tema": "Solución", "mensaje": "Aplicación full stack que registra y clasifica solicitudes."},
        {"paso": 3, "tema": "Arquitectura", "mensaje": "Frontend web, backend Python, SQLite e integración opcional con una API de IA."},
        {"paso": 4, "tema": "Demostración", "mensaje": "Crear una solicitud de soporte y verificar la categoría asignada."},
        {"paso": 5, "tema": "Demostración", "mensaje": "Crear una solicitud comercial y comprobar su persistencia en la base de datos."},
        {"paso": 6, "tema": "Calidad", "mensaje": "Mostrar validación de correo, manejo de errores y pruebas funcionales."},
        {"paso": 7, "tema": "Cierre", "mensaje": "Explicar despliegue, límites actuales y mejoras futuras."},
    ],
    "checklist": [
        "Aplicación iniciada",
        "Base de datos creada",
        "Formulario probado",
        "Clasificación verificada",
        "Listado actualizado",
        "Errores controlados",
        "URL de despliegue preparada si aplica",
    ],
}

print(json.dumps(presentacion, ensure_ascii=False, indent=2))
