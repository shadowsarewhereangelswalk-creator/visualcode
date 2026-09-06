import json
def construir_prompt(cliente,problema):
    return {"rol":"Asistente de soporte","reglas":["No inventar datos","Responder de forma breve","Escalar cuando falte información"],"cliente":cliente,"problema":problema,"salida":{"tipo":"json","campos":["respuesta","accion"]}}
print(json.dumps(construir_prompt("Karen","No puedo iniciar sesión"),ensure_ascii=False,indent=2))
