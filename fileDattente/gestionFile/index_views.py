
from django.http import HttpResponse
from django.shortcuts import render


def auth(request):
    return render(request, 'auth.html')


def index(request):
    return render(request, 'accueil.html')
    # print('****************************salut***************************')
