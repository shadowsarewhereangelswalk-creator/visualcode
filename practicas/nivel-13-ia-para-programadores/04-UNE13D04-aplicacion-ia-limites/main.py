problemas=[{"nombre":"Clasificar mensajes","datos":True,"patrones":True},{"nombre":"Sumar facturas","datos":True,"patrones":False},{"nombre":"Generar respuestas","datos":True,"patrones":True}]
for p in problemas:
    p["recomienda_ia"]=p["datos"] and p["patrones"]
    print(p)
