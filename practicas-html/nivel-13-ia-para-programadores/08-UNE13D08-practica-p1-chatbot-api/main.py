import json,os,urllib.request
url=os.getenv("AI_API_URL","https://api.openai.com/v1/chat/completions")
clave=os.getenv("AI_API_KEY","")
modelo=os.getenv("AI_MODEL","gpt-4.1-mini")
def preguntar(pregunta):
    if not clave:
        return {"respuesta":"Configura AI_API_KEY para ejecutar la llamada real"}
    datos=json.dumps({"model":modelo,"messages":[{"role":"user","content":pregunta}]}).encode()
    req=urllib.request.Request(url,data=datos,headers={"Authorization":f"Bearer {clave}","Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=30) as r:
        salida=json.loads(r.read().decode())
    return {"respuesta":salida["choices"][0]["message"]["content"]}
print(json.dumps(preguntar("Explica qué es una API en una frase"),ensure_ascii=False,indent=2))
