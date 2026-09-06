import json,re
def procesar(nombre,correo,mensaje):
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}",correo) is None: raise ValueError("Correo inválido")
    t=mensaje.lower()
    categoria="soporte" if any(p in t for p in ("error","problema","no funciona")) else "ventas" if any(p in t for p in ("precio","comprar")) else "general"
    return {"nombre":nombre.strip(),"correo":correo.lower(),"mensaje":mensaje.strip(),"categoria":categoria,"requiere_humano":categoria=="soporte"}
print(json.dumps(procesar("Karen","karen@ejemplo.com","La cuenta no funciona"),ensure_ascii=False,indent=2))
