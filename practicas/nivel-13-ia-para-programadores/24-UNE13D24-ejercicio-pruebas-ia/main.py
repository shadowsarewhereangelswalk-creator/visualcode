def normalizar(texto): return " ".join(texto.strip().lower().split())
casos=[("  Hola Mundo  ","hola mundo"),("UNO   DOS","uno dos"),(" prueba ","prueba")]
for entrada,esperado in casos:
    obtenido=normalizar(entrada)
    assert obtenido==esperado
    print(obtenido)
