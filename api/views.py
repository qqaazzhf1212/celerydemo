from django.shortcuts import render
from django.http import JsonResponse
from api.tasks import add, test, test1


# Create your views here.
def info(request):
    # add.delay(2, 2)
    test1.delay()
    # test()
    return JsonResponse({'msg': 'This is ok'})
