import json
def validar_salida(data):
    requeridos={"mensaje","categoria","requiere_humano"}
    return requeridos.issubset(data) and isinstance(data["requiere_humano"],bool)
muestras=[{"mensaje":"Hola","categoria":"general","requiere_humano":False},{"mensaje":"Error","categoria":"soporte","requiere_humano":True}]
assert all(validar_salida(item) for item in muestras)
print(json.dumps({"nivel":13,"estado":"validado","pruebas":len(muestras)},ensure_ascii=False))
