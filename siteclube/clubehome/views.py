from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'clubehome/homepage.html')

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
