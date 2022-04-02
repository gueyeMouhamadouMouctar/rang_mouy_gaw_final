
from django.http import HttpResponse
from django.shortcuts import render

from fileDattente import fileDattente

from .models import ClientQueueManager


def show(request):
    return HttpResponse('salut show')


def start(request):
    return HttpResponse('salut start')


def listeFA(request):
    fileDattente = ClientQueueManager().get_all_clients()
    print(fileDattente)
    return render(request, 'espace_superviseur.html',  {'listeFileDattente': fileDattente})
