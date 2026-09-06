def normalizar_nombre(nombre):
    return " ".join(parte.capitalize() for parte in nombre.strip().split())
def crear_usuario(nombre,correo):
    correo=correo.strip().lower()
    if "@" not in correo: raise ValueError("Correo inválido")
    return {"nombre":normalizar_nombre(nombre),"correo":correo}
print(crear_usuario("  karen agostini ","KAREN@EJEMPLO.COM"))
