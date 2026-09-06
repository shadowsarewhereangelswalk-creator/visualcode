from django.db import models


class Venta(models.Model):
    producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=60)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return self.producto

