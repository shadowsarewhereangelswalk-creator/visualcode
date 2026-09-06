imagen=[[10,10,10,240,240],[10,10,20,230,240],[10,20,30,220,230],[20,30,40,210,220]]
for fila in imagen:
    print(["oscuro" if pixel<128 else "claro" for pixel in fila])
