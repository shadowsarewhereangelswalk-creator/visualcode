import json
def respuesta(ruta):
    rutas={"/":{"status":"ok"},"/solicitudes":{"items":[]},"/health":{"status":"healthy"}}
    return json.dumps(rutas.get(ruta,{"error":"not_found"}),ensure_ascii=False)
for ruta in ["/","/solicitudes","/x"]: print(ruta,respuesta(ruta))
