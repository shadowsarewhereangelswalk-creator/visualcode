from django.http import JsonResponse
from django.shortcuts import render


NOTICIAS = [
    {"id": 1, "titulo": "Django organiza el backend", "categoria": "python"},
    {"id": 2, "titulo": "URLs limpias y mantenibles", "categoria": "web"},
    {"id": 3, "titulo": "ORM para consultas expresivas", "categoria": "datos"},
]


def lista(request):
    return render(request, "core/noticias.html", {"noticias": NOTICIAS})


def detalle(request, noticia_id):
    noticia = next((item for item in NOTICIAS if item["id"] == noticia_id), None)
    return JsonResponse(noticia or {"error": "No encontrada"}, status=200 if noticia else 404)


def buscar(request):
    termino = request.GET.get("q", "").strip().lower()
    resultados = [noticia for noticia in NOTICIAS if termino in noticia["titulo"].lower()]
    return JsonResponse({"q": termino, "resultados": resultados})

