rutas={"ventas":["precio","comprar","cotización"],"soporte":["error","fallo","no funciona"],"facturación":["factura","cobro","pago"]}
def enrutar(texto):
    t=texto.lower()
    for ruta,palabras in rutas.items():
        if any(p in t for p in palabras): return ruta
    return "general"
for mensaje in ["Quiero comprar","La app no funciona","Tengo un cobro"]:
    print(mensaje,enrutar(mensaje))
