def evaluar(sistema,aprende,predice):
    usa_ia=aprende or predice
    limite="Requiere validación humana" if usa_ia else "Resultado determinista"
    return {"sistema":sistema,"usa_ia":usa_ia,"limite":limite}
for caso in [("Buscador",False,False),("Recomendador",True,True),("Clasificador",True,True)]:
    print(evaluar(*caso))
