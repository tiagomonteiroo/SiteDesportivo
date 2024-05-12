from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import (UserDetails, Noticia, Product, Jogo, Coach, Player)
from django.contrib.auth import logout as auth_logout

# Create your views here.
def homepage(request):
    ultimos_jogos = Jogo.objects.order_by('-data_jogo')[:4]
    context = {'ultimos_jogos': ultimos_jogos}
    return render(request, 'clubehome/homepage.html', context)

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
def logout(request):
    auth_logout(request)
    return redirect('homepage')



def criar_noticia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')
        data_publicacao = request.POST.get('data_publicacao')
        Noticia.objects.create(titulo=titulo, descricao=descricao, imagem=imagem, data_publicacao=data_publicacao)
        return redirect('noticias')
    return render(request, 'clubehome/criar_noticia.html')

def criar_jogo(request):
    if request.method == 'POST':
        adversario = request.POST.get('adversario')
        golos_clube = request.POST.get('golos_clube')
        golos_adversario = request.POST.get('golos_adversario')
        local = request.POST.get('local')
        data_jogo = request.POST.get('data_jogo')
        Jogo.objects.create(adversario=adversario, golos_clube=golos_clube, golos_adversario=golos_adversario, local=local,data_jogo=data_jogo)
        return redirect('homepage')
    return render(request, 'clubehome/criar_jogo.html')

def criar_jogador(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        posicao = request.POST.get('posicao')
        if nome and idade and posicao:
            Player.objects.create(number=numero, name=nome, age=idade, position=posicao)
            return redirect('plantel')
        else:
            return render(request, 'clubehome/criar_jogador.html',{'error_message': 'Todos os campos são obrigatórios!'})
    return render(request, 'clubehome/criar_jogador.html')

def criar_treinador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        idade = request.POST.get('idade')
        principal = request.POST.get('principal') == 'on'
        Coach.objects.create(name=nome, job=cargo, age=idade, main=principal)
        return redirect('plantel')
    return render(request, 'clubehome/criar_treinador.html')

def ultimas_noticias(request):
    ultimas_noticias = Noticia.objects.order_by('-data_publicacao')[:6]
    context = {'ultimas_noticias': ultimas_noticias}
    return render(request, 'clubehome/noticias.html', context)

def loja(request):
    produtos = Product.objects.all()
    context = {'produtos' : produtos}
    return render(request, "clubehome/loja.html", context)

def criar_produto (request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")
        tipo = request.POST.get("tipo")
        imagem = request.FILES.get("imagem")
        Product.objects.create(nome=nome,preco=preco, imagem=imagem ,tipo=tipo)
        return redirect('loja')
    return render(request, 'clubehome/criar_produto.html')

def plantel(request):
    jogadores = Player.objects.all()
    treinadores = Coach.objects.all()
    posicoes = ["Guarda-Redes", "Lateral", "Central", "Médio", "Extremo", "Avançado"]
    return render(request, 'clubehome/plantel.html', {'posicoes': posicoes, 'jogadores': jogadores, 'treinadores': treinadores})

def bilhetes(request):
    return render(request, "clubehome/bilhetes.html")

def noticias(request):
    return render(request, "clubehome/noticias.html")

def clube(request):
    return render(request, "clubehome/clube.html")

def socio(request):
    return render(request, "clubehome/socio.html")

def torna_socio(request):
    if request.method == "POST":
        user = request.user
        detalhes = UserDetails.objects.get(user=user)
        detalhes.is_socio = True
        detalhes.save()
        return redirect('socio')
    return render(request, "clubehome/tornasocio.html")

def deixa_socio(request):
    if request.method == "POST":
        user = request.user
        detalhes = UserDetails.objects.get(user=user)
        detalhes.is_socio = False
        detalhes.save()
        return redirect('socio')
    return render(request, "clubehome/tornasocio.html")
