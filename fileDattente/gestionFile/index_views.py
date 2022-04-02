
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Personnel

def auth(request):
    return render(request, 'auth.html')
def login(request):
     
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
             
        try:
            user = Personnel.empAuth_objects.get(email=email,password=password)
            if user is not None:
                profile = user.profil
                
                if profile == 'Agent comptoir':
                    return render(request, 'espace_guichet.html', {})
                elif profile == 'Superviseur':
                    return render(request, 'espace_superviseur.html', {})
            
            else:
                print("Someone tried to login and failed.")
                print("They used Email: {} and password: {}".format(email,password))
     
                #return redirect('/')
                return HttpResponse("C'est pas bon")
        except Exception as identifier:
                
                return redirect('/')
                
     
        else:
            return HttpResponse("C'est pas bon")
           # return render(request, 'base.html')


def index(request):
    return render(request, 'accueil.html')
    # print('****************************salut***************************')
