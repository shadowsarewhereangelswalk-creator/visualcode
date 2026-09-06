from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    publicado = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

