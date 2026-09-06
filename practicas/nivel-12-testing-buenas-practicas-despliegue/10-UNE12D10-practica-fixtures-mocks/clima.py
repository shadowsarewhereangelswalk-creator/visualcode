def obtener_recomendacion(ciudad, cliente, limite=28):
    respuesta = cliente.consultar(ciudad)
    temperatura = float(respuesta["temperatura"])
    if temperatura >= limite:
        mensaje = "Usa ropa fresca"
    elif temperatura <= 15:
        mensaje = "Lleva abrigo"
    else:
        mensaje = "Clima templado"
    return {"ciudad": ciudad, "temperatura": temperatura, "recomendacion": mensaje}
