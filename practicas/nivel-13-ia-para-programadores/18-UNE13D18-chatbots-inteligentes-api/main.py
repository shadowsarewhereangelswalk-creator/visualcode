estado={"tema":None}
def responder(mensaje):
    texto=mensaje.lower()
    if "factura" in texto:
        estado["tema"]="facturación"; return "Indica el número de orden"
    if "soporte" in texto or "error" in texto:
        estado["tema"]="soporte"; return "Describe el problema técnico"
    return "¿En qué puedo ayudarte?"
for mensaje in ["Hola","Tengo un error de soporte"]:
    print(responder(mensaje))
print(estado)
