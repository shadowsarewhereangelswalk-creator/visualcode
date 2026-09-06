from django.http import JsonResponse

from .models import Autor


def relaciones(request):
    autores = Autor.objects.select_related("perfil").prefetch_related("articulos__categorias")
    datos = [
        {
            "autor": autor.nombre,
            "biografia": autor.perfil.biografia if hasattr(autor, "perfil") else "",
            "articulos": [{"titulo": articulo.titulo, "categorias": [categoria.nombre for categoria in articulo.categorias.all()]} for articulo in autor.articulos.all()],
        }
        for autor in autores
    ]
    return JsonResponse({"relaciones": {"uno_a_uno": "perfil", "uno_a_muchos": "articulos", "muchos_a_muchos": "categorias"}, "autores": datos})

