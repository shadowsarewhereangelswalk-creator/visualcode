def categoria(texto):
    t=texto.lower()
    if "error" in t or "problema" in t: return "soporte"
    if "precio" in t or "comprar" in t: return "ventas"
    return "general"
casos={"Tengo un error":"soporte","Quiero precio":"ventas","Hola":"general"}
for entrada,esperado in casos.items(): assert categoria(entrada)==esperado
print({"nivel":14,"estado":"completado","pruebas":len(casos)})
