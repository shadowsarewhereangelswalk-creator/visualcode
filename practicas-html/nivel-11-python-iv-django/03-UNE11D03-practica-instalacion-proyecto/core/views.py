from django.shortcuts import render


def inicio(request):
    contexto = {"titulo": "Mi primer portal Django", "tecnologias": ["Python", "Django", "SQLite"]}
    return render(request, "core/inicio.html", contexto)

