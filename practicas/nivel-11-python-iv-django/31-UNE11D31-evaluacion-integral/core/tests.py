from django.test import TestCase
from django.urls import reverse

from .forms import IncidenciaForm
from .models import Incidencia


class EvaluacionIntegralTests(TestCase):
    def test_modelo(self):
        incidencia = Incidencia.objects.create(titulo="Corregir formulario", prioridad="alta")
        self.assertEqual(str(incidencia), "Corregir formulario")

    def test_validacion(self):
        self.assertFalse(IncidenciaForm({"titulo": "x", "prioridad": "media"}).is_valid())
        self.assertTrue(IncidenciaForm({"titulo": "Error corregido", "prioridad": "baja"}).is_valid())

    def test_vista_crea_registro(self):
        respuesta = self.client.post(reverse("inicio"), {"titulo": "Revisar migración", "prioridad": "alta"})
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Incidencia.objects.count(), 1)

    def test_api_filtra(self):
        Incidencia.objects.create(titulo="Alta prioridad", prioridad="alta")
        Incidencia.objects.create(titulo="Baja prioridad", prioridad="baja")
        respuesta = self.client.get(reverse("api"), {"prioridad": "alta"})
        self.assertEqual(respuesta.json()["total"], 1)

    def test_paginas(self):
        self.assertEqual(self.client.get(reverse("inicio")).status_code, 200)
        self.assertEqual(self.client.get(reverse("api")).status_code, 200)

