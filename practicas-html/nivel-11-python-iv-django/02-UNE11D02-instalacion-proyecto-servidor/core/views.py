from django.http import HttpResponse, JsonResponse


def inicio(request):
    return HttpResponse("<h1>Proyecto Django funcionando</h1><p>El servidor de desarrollo está listo.</p>")


def salud(request):
    return JsonResponse({"estado": "ok", "framework": "Django"})

