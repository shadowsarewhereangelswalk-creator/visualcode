import json
def validar_respuesta(texto):
    data=json.loads(texto)
    if not {"respuesta","accion"}.issubset(data): raise ValueError("Faltan campos")
    return data
print(validar_respuesta('{"respuesta":"Revisa tu correo","accion":"verificar"}'))
