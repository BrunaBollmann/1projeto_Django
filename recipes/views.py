from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'bruna bollmann',
    })


def contato(request):
    return render(request, 'me_apage/temp.html')


def sobre(request):
    return HttpResponse('Hello Django world sobre')
