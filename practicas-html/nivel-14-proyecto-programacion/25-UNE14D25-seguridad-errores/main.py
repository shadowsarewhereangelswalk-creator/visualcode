import re
def validar(nombre,correo,mensaje):
    if len(nombre.strip())<3: raise ValueError("Nombre inválido")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}",correo.strip()) is None: raise ValueError("Correo inválido")
    if len(mensaje.strip())<10: raise ValueError("Mensaje demasiado corto")
    return {"nombre":nombre.strip(),"correo":correo.strip().lower(),"mensaje":mensaje.strip()}
print(validar("Karen Agostini","karen@ejemplo.com","Necesito información"))
