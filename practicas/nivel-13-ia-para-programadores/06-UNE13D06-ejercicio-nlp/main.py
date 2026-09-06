positivas={"excelente","bien","gracias","rápido"}
negativas={"mal","error","lento","problema"}
def sentimiento(texto):
    palabras=set(texto.lower().split())
    puntaje=len(palabras & positivas)-len(palabras & negativas)
    return "positivo" if puntaje>0 else "negativo" if puntaje<0 else "neutral"
for t in ["excelente servicio gracias","tengo un error y problema","consulta general"]:
    print(t,sentimiento(t))
