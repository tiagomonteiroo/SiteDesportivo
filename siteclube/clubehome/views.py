from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Treinador, Jogador

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
    return render(request,'clubehome/login.html')

def criar_utilizador(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_admin = request.POST.get('is_admin') == 'on'
        is_socio = request.POST.get('is_socio') == 'on'
        NIF = request.POST.get('NIF')
        user = User.objects.create_user(username=username, password=password)
        UserDetails.objects.create(user=user, is_admin=is_admin, is_socio=is_socio, NIF=NIF)
        return redirect('homepage')
    return render(request, 'clubehome/criar_utilizador.html')

def plantel_view(request):
    # Obter todos os treinadores e jogadores do banco de dados
    treinadores = Treinador.objects.all()
    jogadores = Jogador.objects.all()
    return render(request, 'clubehome/plantel.html', {'treinadores': treinadores, 'jogadores': jogadores})

def loja(request):
    return render(request, "clubehome/loja.html")

def bilhetes(request):
    return render(request, "clubehome/bilhetes.html")

def noticias(request):
    return render(request, "clubehome/noticias.html")

def clube(request):
    return render(request, "clubehome/clube.html")

def socio(request):
    return render(request, "clubehome/socio.html")
