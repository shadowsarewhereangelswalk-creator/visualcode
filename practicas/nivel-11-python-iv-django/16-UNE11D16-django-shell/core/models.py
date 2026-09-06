from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nivel = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

