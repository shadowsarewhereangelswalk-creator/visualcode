from django.http import JsonResponse


def inicio(request):
    practicas = [
        {"codigo": "P1", "dia": 8, "entrega": "Proyecto con modelos y migraciones"},
        {"codigo": "P2", "dia": 15, "entrega": "CRUD con ORM"},
        {"codigo": "P3", "dia": 22, "entrega": "Templates y formularios"},
        {"codigo": "P4", "dia": 26, "entrega": "API REST con DRF"},
        {"codigo": "P5", "dia": 30, "entrega": "Aplicación web completa"},
    ]
    return JsonResponse({"nivel": 11, "clases": 31, "proyecto": "Aplicación Django", "practicas": practicas})

