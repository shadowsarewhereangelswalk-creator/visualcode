from django.db import models


class Oferta(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=20, choices=[("remoto", "Remoto"), ("hibrido", "Híbrido"), ("presencial", "Presencial")])
    salario = models.PositiveIntegerField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cargo} · {self.empresa}"

