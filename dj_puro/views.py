from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from dj_puro.models import Categoria


def categoria_list(request):
    MAX_OBJECTS = 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]
    data = {"result": list(cat.values("descripcion", "activo"))}

    return JsonResponse(data)


def categoria_detalle(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {
        "result": {
                 "descripcion": cat.descripcion,
                 "activo": cat.activo,
                }
        }

    return JsonResponse(data)


