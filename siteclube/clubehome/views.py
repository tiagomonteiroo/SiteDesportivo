from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render(request, 'clubehome/homepage.html')

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            error_message = "Nome de usuário ou senha incorretos."
            return render(request, 'clubehome/login.html', {'error_message': error_message})
    return render(request,'clubehome/login.html' )

def loja(request):
    return render(request, "clubehome/loja.html")

def plantel(request):
    return render(request, "clubehome/plantel.html")

def bilhetes(request):
    return render(request, "clubehome/bilhetes.html")

def noticias(request):
    return render(request, "clubehome/noticias.html")

def resultados(request):
    return render(request, "clubehome/resultados.html")

def clube(request):
    return render(request, "clubehome/clube.html")

def socio(request):
    return render(request, "clubehome/socio.html")
