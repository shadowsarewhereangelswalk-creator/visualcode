from rest_framework.test import APITestCase


class ViewSetTests(APITestCase):
    def test_relacion_y_resumen(self):
        cliente = self.client.post("/api/clientes/", {"nombre": "Ada", "correo": "ada@career.dev"}, format="json").data
        creada = self.client.post("/api/proyectos/", {"cliente": cliente["id"], "nombre": "Portal", "estado": "activo", "presupuesto": "1500.00"}, format="json")
        self.assertEqual(creada.status_code, 201)
        self.assertEqual(self.client.get("/api/proyectos/resumen/").data["proyectos"], 1)
        self.assertEqual(self.client.get(f"/api/clientes/{cliente['id']}/").data["total_proyectos"], 1)

