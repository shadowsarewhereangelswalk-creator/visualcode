from django.db import models


class Incidencia(models.Model):
    titulo = models.CharField(max_length=120)
    prioridad = models.CharField(max_length=10, choices=[("baja", "Baja"), ("media", "Media"), ("alta", "Alta")], default="media")
    resuelta = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

