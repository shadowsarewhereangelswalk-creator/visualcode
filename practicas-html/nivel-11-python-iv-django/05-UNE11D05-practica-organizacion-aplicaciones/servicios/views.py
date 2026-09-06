from django.shortcuts import render


def lista(request):
    servicios = ["Desarrollo web", "Automatización", "Datos"]
    return render(request, "servicios/lista.html", {"servicios": servicios})

