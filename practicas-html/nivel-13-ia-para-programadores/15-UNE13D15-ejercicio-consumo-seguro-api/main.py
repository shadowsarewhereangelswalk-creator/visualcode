import json
def preparar_peticion(modelo,prompt):
    if not modelo or not prompt.strip(): raise ValueError("Datos incompletos")
    return json.dumps({"model":modelo,"messages":[{"role":"user","content":prompt.strip()}]},ensure_ascii=False)
print(preparar_peticion("modelo-demo","Resume este texto"))
