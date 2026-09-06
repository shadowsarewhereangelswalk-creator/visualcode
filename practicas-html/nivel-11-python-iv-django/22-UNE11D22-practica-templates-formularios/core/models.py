from django.db import models


class Reserva(models.Model):
    nombre = models.CharField(max_length=80)
    correo = models.EmailField()
    servicio = models.CharField(max_length=30, choices=[("mentoria", "Mentoría"), ("portafolio", "Portafolio"), ("entrevista", "Entrevista")])
    fecha = models.DateField()
    mensaje = models.TextField(blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} · {self.fecha}"

