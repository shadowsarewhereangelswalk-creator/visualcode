import unittest

from calculadora import dividir, promedio, sumar


class CalculadoraTests(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(7, 5), 12)

    def test_dividir(self):
        self.assertAlmostEqual(dividir(9, 2), 4.5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(3, 0)

    def test_promedio(self):
        self.assertEqual(promedio([2, 4, 6]), 4)


if __name__ == "__main__":
    unittest.main()
