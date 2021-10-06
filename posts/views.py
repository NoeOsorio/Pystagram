from datetime import datetime
import json
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import render
from posts.models import PostModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def list(request: HttpRequest):
    # posts = [
    #     {
    #         'name': 'My Dog.',
    #         'user': 'Yésica Cortes',
    #         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    #         'picture': 'https://picsum.photos/id/237/200/200'
    #     },
    #     {
    #         'name': 'Khe.',
    #         'user': 'Pink Woman',
    #         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    #         'picture': 'https://picsum.photos/id/84/200/200'
    #     },
    #     {
    #         'name': 'Nautural web.',
    #         'user': 'Pancho Villa',
    #         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    #         'picture': 'https://picsum.photos/id/784/200/200'
    #     },

    # ]

    posts = PostModel.objects.all()
    posts = [post.json() for post in posts]

    return JsonResponse({'posts': posts})


@csrf_exempt
def update(request: HttpRequest, id: int):
    data = json.loads(request.body)
    post: PostModel = PostModel.objects.get(pk=id)
    post.title = data['title']

    post.save()
    return HttpResponse("ACTUALIZAD CORRECTAMENTE")
