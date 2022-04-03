
from django.http import HttpResponse
from django.shortcuts import render

from fileDattente import fileDattente

from .models import ClientQueueManager


def guichets(request):
    return render(request, 'espace_guichet.html')


def vigile(request):
    return render(request, 'espace_vigile.html')


def caisse(request, numGuichet=0):
    if request.method == 'POST':
        numero = request.POST['numero']
        request.session['numero'] = numero
    return render(request, 'espace_caisse.html')


def listeFA(request):
    fileDattente = ClientQueueManager().get_all_clients()
    print(fileDattente)
    return render(request, 'espace_caisse.html',  {'listeFileDattente': fileDattente})


def passer_au_client_suiv(request):
    ClientQueueManager().pop_first_client()
    return render(request, 'espace_caisse.html')
