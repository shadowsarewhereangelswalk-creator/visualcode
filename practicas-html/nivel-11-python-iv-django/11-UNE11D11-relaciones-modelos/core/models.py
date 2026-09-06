from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE, related_name="perfil")
    biografia = models.TextField(blank=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="articulos")
    categorias = models.ManyToManyField(Categoria, related_name="articulos", blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

