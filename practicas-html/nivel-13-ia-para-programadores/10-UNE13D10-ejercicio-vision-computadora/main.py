imagen=[[10,10,10,240,240],[10,10,20,230,240],[10,20,30,220,230],[20,30,40,210,220]]
bordes=[]
for fila in imagen:
    bordes.append([abs(pixel-(fila[i-1] if i else pixel)) for i,pixel in enumerate(fila)])
for fila in bordes:
    print(fila)
