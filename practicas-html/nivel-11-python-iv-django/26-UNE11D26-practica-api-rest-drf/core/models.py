from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

