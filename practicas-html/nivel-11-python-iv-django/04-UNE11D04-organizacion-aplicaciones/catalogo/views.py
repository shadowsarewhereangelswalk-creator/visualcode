from django.http import JsonResponse


def lista(request):
    return JsonResponse({"productos": ["Curso Python", "Curso Django", "Mentoría"]})

