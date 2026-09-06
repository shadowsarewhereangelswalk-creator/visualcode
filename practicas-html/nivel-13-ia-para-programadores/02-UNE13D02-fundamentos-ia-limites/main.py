casos=[("Filtro de spam basado en reglas",False,"No aprende por sí solo"),("Clasificador entrenado con ejemplos",True,"Puede cometer errores"),("Calculadora tradicional",False,"Sigue reglas deterministas")]
for nombre,usa_ia,limite in casos:
    print(nombre,"|","IA" if usa_ia else "No IA","|",limite)
