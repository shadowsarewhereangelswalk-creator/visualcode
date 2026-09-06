from calculos import calcular_total
from formatos import crear_codigo, moneda, normalizar_nombre


def crear_venta(numero, cliente, servicio, precio, cantidad):
    nombre = normalizar_nombre(cliente)
    return {
        "codigo": crear_codigo(nombre, numero),
        "cliente": nombre,
        "servicio": servicio.strip().title(),
        "cantidad": cantidad,
        "total": calcular_total(precio, cantidad, descuento=0.08),
    }


def main():
    venta = crear_venta(42, "  ana   torres ", "automatización", 275, 4)
    print(f'Código: {venta["codigo"]}')
    print(f'Cliente: {venta["cliente"]}')
    print(f'Servicio: {venta["servicio"]} x {venta["cantidad"]}')
    print(f'Total: {moneda(venta["total"])}')


if __name__ == "__main__":
    main()
