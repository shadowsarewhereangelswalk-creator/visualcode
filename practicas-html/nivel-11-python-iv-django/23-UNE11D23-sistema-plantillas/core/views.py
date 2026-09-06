from django.shortcuts import render


def inicio(request):
    proyectos = [
        {"nombre": "Portafolio", "estado": "listo", "avance": 100},
        {"nombre": "API de empleos", "estado": "activo", "avance": 72},
        {"nombre": "Panel de datos", "estado": "nuevo", "avance": 15},
    ]
    return render(request, "core/inicio.html", {"proyectos": proyectos, "promedio": 62})

