from utilidades import (
    calcular_cotizacion,
    crear_codigo,
    formatear_moneda,
    normalizar_nombre,
    validar_correo,
)


def generar_resumen(numero, nombre, correo, servicio, precio, cantidad):
    cliente = normalizar_nombre(nombre)
    if not validar_correo(correo):
        raise ValueError("El correo no es válido")
    detalle = calcular_cotizacion(precio, cantidad, descuento=0.1)
    return {
        "codigo": crear_codigo(cliente, numero),
        "cliente": cliente,
        "correo": correo.strip().lower(),
        "servicio": servicio.strip().title(),
        "detalle": detalle,
    }


def main():
    resumen = generar_resumen(
        27,
        "  karen   ramírez ",
        "karen@ejemplo.com",
        "automatización de procesos",
        325,
        3,
    )
    print(f'Código: {resumen["codigo"]}')
    print(f'Cliente: {resumen["cliente"]} · {resumen["correo"]}')
    print(f'Servicio: {resumen["servicio"]}')
    for concepto, valor in resumen["detalle"].items():
        print(f"{concepto.title()}: {formatear_moneda(valor)}")


if __name__ == "__main__":
    main()
