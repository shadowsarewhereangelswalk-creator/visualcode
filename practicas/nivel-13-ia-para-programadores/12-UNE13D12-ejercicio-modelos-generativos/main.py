import random
vocabulario={"marketing":["campaña","audiencia","conversión"],"programación":["función","variable","prueba"],"ia":["modelo","prompt","respuesta"]}
def generar(tema,cantidad=5):
    base=vocabulario[tema]
    return " ".join(random.choice(base) for _ in range(cantidad))
for tema in vocabulario:
    print(tema,":",generar(tema))
