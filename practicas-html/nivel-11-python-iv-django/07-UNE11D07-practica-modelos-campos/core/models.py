from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    categoria = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

