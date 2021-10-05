from datetime import datetime
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def list(request):
    posts = [
        {
            'name': 'My Dog.',
            'user': 'Yésica Cortes',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/id/237/200/200'
        },
        {
            'name': 'Khe.',
            'user': 'Pink Woman',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/id/84/200/200'
        },
        {
            'name': 'Nautural web.',
            'user': 'Pancho Villa',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/id/784/200/200'
        },

    ]
    return JsonResponse({'posts': posts})
