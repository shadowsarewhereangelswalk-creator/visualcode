from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    precio_desde = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, related_name="solicitudes")
    nombre = models.CharField(max_length=80)
    correo = models.EmailField()
    mensaje = models.TextField()
    estado = models.CharField(max_length=20, choices=[("nueva", "Nueva"), ("contactada", "Contactada"), ("cerrada", "Cerrada")], default="nueva")
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} · {self.servicio}"

