from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")
    nombre = models.CharField(max_length=120)
    estado = models.CharField(max_length=20, choices=[("planeado", "Planeado"), ("activo", "Activo"), ("entregado", "Entregado")], default="planeado")
    etiquetas = models.ManyToManyField(Etiqueta, related_name="proyectos", blank=True)

    def __str__(self):
        return self.nombre

