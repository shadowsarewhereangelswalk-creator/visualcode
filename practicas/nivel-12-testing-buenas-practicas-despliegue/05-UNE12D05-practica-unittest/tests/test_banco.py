import unittest
from decimal import Decimal

from banco import Cuenta


class CuentaTests(unittest.TestCase):
    def setUp(self):
        self.cuenta = Cuenta("Ana", 100)

    def test_depositar(self):
        self.assertEqual(self.cuenta.depositar(25.5), Decimal("125.5"))

    def test_retirar(self):
        self.assertEqual(self.cuenta.retirar(40), Decimal("60"))

    def test_operaciones_invalidas(self):
        for operacion, monto in (
            (self.cuenta.depositar, 0),
            (self.cuenta.retirar, 101),
        ):
            with self.subTest(monto=monto):
                with self.assertRaises(ValueError):
                    operacion(monto)


if __name__ == "__main__":
    unittest.main()
