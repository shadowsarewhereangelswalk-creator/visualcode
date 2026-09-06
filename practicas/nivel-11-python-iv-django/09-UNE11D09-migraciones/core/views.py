from django.db import connection
from django.http import JsonResponse

from .models import Cliente


def estado(request):
    tablas = connection.introspection.table_names()
    return JsonResponse({"modelo": Cliente.__name__, "tabla": Cliente._meta.db_table, "migrada": Cliente._meta.db_table in tablas})

