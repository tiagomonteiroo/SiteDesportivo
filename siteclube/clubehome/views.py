from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'clubehome/homepage.html')

def loja(request):
    return render(request, "clubehome/loja.html")

def plantel(request):
    return render(request, "clubehome/plantel.html")