import json

from django.test import TestCase


class NotaRestTests(TestCase):
    def test_ciclo_completo(self):
        creada = self.client.post("/api/notas/", data=json.dumps({"titulo": "Primera nota", "contenido": "Contenido completo"}), content_type="application/json")
        self.assertEqual(creada.status_code, 201)
        nota_id = creada.json()["id"]
        editada = self.client.patch(f"/api/notas/{nota_id}/", data=json.dumps({"titulo": "Nota editada"}), content_type="application/json")
        self.assertEqual(editada.json()["titulo"], "Nota editada")
        self.assertEqual(self.client.delete(f"/api/notas/{nota_id}/").status_code, 204)

