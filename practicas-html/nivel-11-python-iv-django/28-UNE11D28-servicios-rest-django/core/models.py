from django.db import models


class Nota(models.Model):
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    creada_en = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {"id": self.pk, "titulo": self.titulo, "contenido": self.contenido, "creada_en": self.creada_en.isoformat()}

