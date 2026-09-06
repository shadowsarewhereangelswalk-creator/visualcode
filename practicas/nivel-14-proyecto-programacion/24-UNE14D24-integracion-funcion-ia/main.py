import json
import os
import urllib.error
import urllib.request

CATEGORIAS = {"soporte", "ventas", "general"}


def clasificar_local(texto):
    contenido = texto.lower()
    if any(palabra in contenido for palabra in ("error", "no funciona", "problema", "fallo")):
        return "soporte"
    if any(palabra in contenido for palabra in ("precio", "comprar", "cotización", "contratar")):
        return "ventas"
    return "general"


def clasificar_con_ia(texto):
    url = os.getenv("AI_API_URL", "").strip()
    clave = os.getenv("AI_API_KEY", "").strip()
    modelo = os.getenv("AI_MODEL", "").strip()
    if not url or not clave or not modelo:
        return {"categoria": clasificar_local(texto), "fuente": "local"}
    datos = json.dumps({
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Clasifica el mensaje en una sola categoría: soporte, ventas o general. Responde únicamente con la categoría."},
            {"role": "user", "content": texto},
        ],
    }).encode("utf-8")
    solicitud = urllib.request.Request(
        url,
        data=datos,
        headers={"Authorization": f"Bearer {clave}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(solicitud, timeout=30) as respuesta:
            salida = json.loads(respuesta.read().decode("utf-8"))
        categoria = salida["choices"][0]["message"]["content"].strip().lower()
        if categoria not in CATEGORIAS:
            raise ValueError("Categoría inesperada")
        return {"categoria": categoria, "fuente": "ia"}
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
        return {"categoria": clasificar_local(texto), "fuente": "local-respaldo"}


for mensaje in ("No funciona mi cuenta", "Quiero una cotización", "Hola, necesito información"):
    print(json.dumps({"mensaje": mensaje, **clasificar_con_ia(mensaje)}, ensure_ascii=False))
