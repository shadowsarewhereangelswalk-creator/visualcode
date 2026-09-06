import random
transiciones={"la":["ia","aplicación"],"ia":["genera","ayuda"],"genera":["texto"],"ayuda":["a"],"a":["programar"],"aplicación":["usa"],"usa":["ia"]}
palabra="la"
salida=[palabra]
for _ in range(8):
    opciones=transiciones.get(palabra)
    if not opciones: break
    palabra=random.choice(opciones)
    salida.append(palabra)
print(" ".join(salida))
