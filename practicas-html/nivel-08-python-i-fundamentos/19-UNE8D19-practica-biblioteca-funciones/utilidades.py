import re
import unicodedata
from decimal import Decimal, ROUND_HALF_UP


def normalizar_nombre(nombre):
    return " ".join(nombre.strip().split()).title()


def crear_codigo(nombre, numero):
    texto = unicodedata.normalize("NFKD", normalizar_nombre(nombre))
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    letras = "".join(palabra[0] for palabra in texto.split()).upper()
    return f"{letras}-{numero:04d}"


def validar_correo(correo):
    patron = r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$"
    return re.fullmatch(patron, correo.strip()) is not None


def calcular_cotizacion(precio, cantidad=1, descuento=0, impuesto=0.16):
    precio = Decimal(str(precio))
    cantidad = Decimal(str(cantidad))
    descuento = Decimal(str(descuento))
    impuesto = Decimal(str(impuesto))
    if precio <= 0 or cantidad <= 0:
        raise ValueError("El precio y la cantidad deben ser positivos")
    subtotal = precio * cantidad
    ahorro = subtotal * descuento
    base = subtotal - ahorro
    tributo = base * impuesto
    total = base + tributo
    moneda = Decimal("0.01")
    return {
        "subtotal": subtotal.quantize(moneda, rounding=ROUND_HALF_UP),
        "descuento": ahorro.quantize(moneda, rounding=ROUND_HALF_UP),
        "impuesto": tributo.quantize(moneda, rounding=ROUND_HALF_UP),
        "total": total.quantize(moneda, rounding=ROUND_HALF_UP),
    }


def formatear_moneda(valor, simbolo="USD"):
    return f"{simbolo} {Decimal(str(valor)):,.2f}"
