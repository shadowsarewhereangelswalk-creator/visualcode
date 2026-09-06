def clasificar(texto):
    t=texto.lower()
    if any(p in t for p in ("error","no funciona","problema")): return "soporte"
    if any(p in t for p in ("precio","comprar","cotización")): return "ventas"
    return "general"
for mensaje in ["No funciona mi cuenta","Quiero precio","Hola"]: print(mensaje,clasificar(mensaje))
