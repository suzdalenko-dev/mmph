from django.http import JsonResponse


def defalt_point(request):
    res = {
        "status": "success",
        "mensaje": "Hola desde Django",
        "usuario": "Pete",
        "items": [10, 20, 30]
    }
    return JsonResponse(res)