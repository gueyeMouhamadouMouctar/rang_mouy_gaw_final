
from django.http import HttpResponse
from django.shortcuts import render

from fileDattente import fileDattente

from .models import ClientQueueManager


def listeFA(request):
    liste = ClientQueueManager().get_all_clients()
    context = {'liste': liste}
    return render(request, 'espace_superviseur.html', context)


def start(request):
    return HttpResponse('salut start')


# def listeFA(request):
#     fileDattente = ClientQueueManager().get_all_clients()
#     print(fileDattente)
#     return render(request, 'espace_superviseur.html',  {'listeFileDattente': fileDattente})
