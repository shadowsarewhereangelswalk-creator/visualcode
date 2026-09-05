import unittest

from main import RepositorioMemoria, validar_datos


class PruebasNivel9(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioMemoria()

    def test_validacion(self):
        self.assertEqual(
            validar_datos(" ana torres ", "ANA@EJEMPLO.COM", "automatización"),
            ("Ana Torres", "ana@ejemplo.com", "Automatización"),
        )

    def test_crear_y_listar(self):
        cliente = self.repositorio.crear("Ana Torres", "ana@ejemplo.com", "Automatización")
        self.assertEqual(self.repositorio.listar(), [cliente])

    def test_correo_unico(self):
        self.repositorio.crear("Ana Torres", "ana@ejemplo.com", "Automatización")
        with self.assertRaises(ValueError):
            self.repositorio.crear("Otra Persona", "ana@ejemplo.com", "Soporte")

    def test_actualizar(self):
        cliente = self.repositorio.crear("Ana Torres", "ana@ejemplo.com", "Automatización")
        actualizado = self.repositorio.actualizar(cliente.id, "Ana Torres", "ana@ejemplo.com", "Desarrollo")
        self.assertEqual(actualizado.servicio, "Desarrollo")

    def test_eliminar(self):
        cliente = self.repositorio.crear("Ana Torres", "ana@ejemplo.com", "Automatización")
        self.assertEqual(self.repositorio.eliminar(cliente.id), cliente)
        self.assertEqual(self.repositorio.listar(), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
