
from django.http import HttpResponse
from django.shortcuts import render


from fileDattente import fileDattente

from .models import ClientQueueManager


def show(request):
    liste = ClientQueueManager().get_all_clients()
    context = {'liste': liste}
    return render(request, 'espace_superviseur.html', context)

def start(request, status=None):
    for i in range(int(ClientQueueManager().get_queue_length())):
        ClientQueueManager().pop_first_client()
    return show(request)


def continuer(request):
    return show(request)

def listeFA(request):
    liste = ClientQueueManager().get_all_clients()
    print(liste)
    return render(request, 'espace_superviseur.html',  {'liste': liste})
