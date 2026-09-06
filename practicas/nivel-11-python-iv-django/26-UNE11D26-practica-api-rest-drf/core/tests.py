from rest_framework import status
from rest_framework.test import APITestCase

from .models import Tarea


class TareaApiTests(APITestCase):
    def test_crud_completo(self):
        creada = self.client.post("/tareas/", {"titulo": "Probar API", "descripcion": "Servicio DRF"}, format="json")
        self.assertEqual(creada.status_code, status.HTTP_201_CREATED)
        tarea_id = creada.data["id"]
        actualizada = self.client.patch(f"/tareas/{tarea_id}/", {"completada": True}, format="json")
        self.assertTrue(actualizada.data["completada"])
        self.assertEqual(self.client.get("/tareas/?completada=true").data["count"], 1)
        self.assertEqual(self.client.delete(f"/tareas/{tarea_id}/").status_code, status.HTTP_204_NO_CONTENT)

    def test_validacion(self):
        respuesta = self.client.post("/tareas/", {"titulo": "x"}, format="json")
        self.assertEqual(respuesta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tarea.objects.count(), 0)

