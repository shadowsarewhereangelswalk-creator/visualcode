from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")
    nombre = models.CharField(max_length=120)
    estado = models.CharField(max_length=20, choices=[("nuevo", "Nuevo"), ("activo", "Activo"), ("cerrado", "Cerrado")], default="nuevo")
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

