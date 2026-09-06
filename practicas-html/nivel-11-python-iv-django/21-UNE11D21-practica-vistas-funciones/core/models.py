from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

