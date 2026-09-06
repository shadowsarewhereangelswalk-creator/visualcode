def validar_historia(historia):
    return all(historia.get(campo) for campo in ("como","quiero","para","aceptacion")) and len(historia["aceptacion"])>0
historia={"como":"usuario","quiero":"crear una solicitud","para":"recibir soporte","aceptacion":["mensaje obligatorio"]}
print(validar_historia(historia))
