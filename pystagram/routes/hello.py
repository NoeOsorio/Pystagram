from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Welcome current time is: {now}'.format(now=str(now)))


def hi(request: HttpRequest):
    # import pdb
    # pdb.set_trace()
    numbers = request.GET['numbers']

    numbers = sorted(numbers.split(","))
    return JsonResponse({"numbers": numbers})
