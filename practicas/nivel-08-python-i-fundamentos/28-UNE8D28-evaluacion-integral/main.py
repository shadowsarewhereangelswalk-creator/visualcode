import re
import unittest
from decimal import Decimal


def validar_codigo(codigo):
    return re.fullmatch(r"CLI-\d{3}", codigo) is not None


def validar_correo(correo):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is not None


def validar_telefono(telefono):
    digitos = re.sub(r"\D", "", telefono)
    return 10 <= len(digitos) <= 15


def calcular_total(precio, cantidad, descuento=0, impuesto=0.16):
    precio = Decimal(str(precio))
    cantidad = Decimal(str(cantidad))
    descuento = Decimal(str(descuento))
    impuesto = Decimal(str(impuesto))
    if precio <= 0 or cantidad <= 0:
        raise ValueError("Precio y cantidad deben ser positivos")
    if not Decimal("0") <= descuento <= Decimal("1"):
        raise ValueError("Descuento fuera de rango")
    return (precio * cantidad * (Decimal("1") - descuento) * (Decimal("1") + impuesto)).quantize(Decimal("0.01"))


class PruebasAplicacion(unittest.TestCase):
    def test_codigo_valido(self):
        self.assertTrue(validar_codigo("CLI-027"))

    def test_codigo_invalido(self):
        self.assertFalse(validar_codigo("cliente-27"))

    def test_correo(self):
        self.assertTrue(validar_correo("karen@ejemplo.com"))
        self.assertFalse(validar_correo("karen@ejemplo"))

    def test_telefono(self):
        self.assertTrue(validar_telefono("+58 412-555-0198"))
        self.assertFalse(validar_telefono("1234"))

    def test_total(self):
        self.assertEqual(calcular_total(100, 2, 0.1), Decimal("208.80"))

    def test_montos_invalidos(self):
        with self.assertRaises(ValueError):
            calcular_total(-10, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
