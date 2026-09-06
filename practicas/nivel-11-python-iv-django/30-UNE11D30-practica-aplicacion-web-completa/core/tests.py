from rest_framework.test import APITestCase

from .models import Servicio, Solicitud


class AplicacionTests(APITestCase):
    def setUp(self):
        self.servicio = Servicio.objects.create(nombre="Automatización", slug="automatizacion", descripcion="Procesos eficientes", precio_desde="500.00")

    def test_formulario_y_panel(self):
        datos = {"servicio": self.servicio.pk, "nombre": "Karen", "correo": "karen@career.dev", "mensaje": "Quiero automatizar mi flujo de trabajo."}
        respuesta = self.client.post("/", datos, follow=True)
        self.assertContains(respuesta, "Solicitud enviada correctamente")
        self.assertContains(self.client.get("/panel/"), "Karen")

    def test_api(self):
        creada = self.client.post("/api/solicitudes/", {"servicio": self.servicio.pk, "nombre": "Ada", "correo": "ada@career.dev", "mensaje": "Necesito una aplicación empresarial.", "estado": "nueva"}, format="json")
        self.assertEqual(creada.status_code, 201)
        self.assertEqual(Solicitud.objects.count(), 1)
        self.assertEqual(self.client.get("/api/servicios/").data["count"], 1)

