import json
import os
import re
import urllib.error
import urllib.request

CATEGORIAS = {"soporte", "ventas", "general"}


def validar_correo(correo):
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo.strip()) is None:
        raise ValueError("Correo inválido")
    return correo.strip().lower()


def clasificar_local(mensaje):
    contenido = mensaje.lower()
    if any(palabra in contenido for palabra in ("error", "problema", "no funciona", "fallo")):
        return "soporte"
    if any(palabra in contenido for palabra in ("precio", "comprar", "cotización", "contratar")):
        return "ventas"
    return "general"


def clasificar_ia(mensaje):
    url = os.getenv("AI_API_URL", "").strip()
    clave = os.getenv("AI_API_KEY", "").strip()
    modelo = os.getenv("AI_MODEL", "").strip()
    if not url or not clave or not modelo:
        return clasificar_local(mensaje), "local"
    cuerpo = json.dumps({
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Clasifica el mensaje como soporte, ventas o general. Responde únicamente con una de esas palabras."},
            {"role": "user", "content": mensaje},
        ],
    }).encode("utf-8")
    solicitud = urllib.request.Request(
        url,
        data=cuerpo,
        headers={"Authorization": f"Bearer {clave}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(solicitud, timeout=30) as respuesta:
            salida = json.loads(respuesta.read().decode("utf-8"))
        categoria = salida["choices"][0]["message"]["content"].strip().lower()
        if categoria not in CATEGORIAS:
            raise ValueError("Categoría inesperada")
        return categoria, "ia"
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
        return clasificar_local(mensaje), "local-respaldo"


def procesar(nombre, correo, mensaje):
    nombre_limpio = " ".join(nombre.split())
    mensaje_limpio = mensaje.strip()
    if len(nombre_limpio) < 2:
        raise ValueError("Nombre inválido")
    if len(mensaje_limpio) < 5:
        raise ValueError("Mensaje demasiado corto")
    categoria, fuente = clasificar_ia(mensaje_limpio)
    return {
        "nombre": nombre_limpio,
        "correo": validar_correo(correo),
        "mensaje": mensaje_limpio,
        "categoria": categoria,
        "fuente_clasificacion": fuente,
        "requiere_humano": categoria == "soporte",
    }


resultado = procesar("Karen Agostini", "karen@ejemplo.com", "La cuenta no funciona desde ayer")
print(json.dumps(resultado, ensure_ascii=False, indent=2))
