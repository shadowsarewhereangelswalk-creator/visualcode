def clasificar(texto):
    t=texto.lower()
    if any(p in t for p in ("urgente","error","fallo")): return "alta"
    if any(p in t for p in ("consulta","pregunta")): return "media"
    return "baja"
casos={"Error urgente en producción":"alta","Tengo una pregunta":"media","Gracias por la ayuda":"baja"}
for entrada,esperado in casos.items():
    obtenido=clasificar(entrada)
    assert obtenido==esperado,(entrada,obtenido,esperado)
    print(entrada,obtenido)
