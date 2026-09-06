def validar_modelo(modelo):
    errores=[]
    for entidad,datos in modelo.items():
        if "pk" not in datos: errores.append(f"{entidad} sin PK")
    return errores
modelo={"usuarios":{"pk":"id"},"solicitudes":{"pk":"id","fk":"usuario_id"}}
print(validar_modelo(modelo))
