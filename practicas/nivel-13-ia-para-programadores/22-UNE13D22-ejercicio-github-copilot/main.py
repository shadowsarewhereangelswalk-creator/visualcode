def promedio(valores):
    if not valores: raise ValueError("La lista no puede estar vacía")
    return sum(valores)/len(valores)
def resumen(valores):
    return {"min":min(valores),"max":max(valores),"promedio":round(promedio(valores),2)}
print(resumen([72,80,91,88,95]))
