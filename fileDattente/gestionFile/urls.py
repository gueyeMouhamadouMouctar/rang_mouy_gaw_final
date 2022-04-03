from django.urls import path
from . import guichet_views, tickets_views, menu, super_views, index_views


urlpatterns = [
    path('', index_views.index, name='index'),
    path('auth', index_views.auth, name='auth'),
    path('guichets', guichet_views.guichets, name='guichets'),
    path('vigiles', guichet_views.vigile, name='vigile'),
    # path('caisse', guichet_views.caisse, name='caisse'),
    path('caisse', guichet_views.listeFA, name='listefileDattenteCaisse'),
    path('clientSuivant', guichet_views.passer_au_client_suiv,
         name='passer_au_client_suiv'),
    path('tickets', tickets_views.tickets, name='tickets'),
    path('show', super_views.show, name='show'),

    path('start', super_views.start, name='start'),
    path('superviseur', super_views.listeFA, name='listefileDattente'),
    path('continue',super_views.continuer,name='continue'),
    #path('', menu.index, name='menu'),


    path('tcs', tickets_views.addClientSImple,
         name='tcs'),
    path('tcSenior', tickets_views.addClientSenior,
         name='tcSenior'),
    path('tcp', tickets_views.addClientPregnant,
         name='tcp'),

]
