from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("login/", views.auth_login, name = "login"),
    path("plantel/", views.plantel_view, name = "plantel"),
    path("loja/", views.loja, name = "loja"),
    path("bilhetes/", views.bilhetes, name = "bilhetes"),
    path("noticias/", views.ultimas_quatro_noticias, name = "noticias"),
    path("clube/", views.clube, name = "clube"),
    path("socio/", views.socio, name = "socio"),
    path("registar/", views.criar_utilizador, name="registar"),
    path("criarnoticia/", views.criar_noticia, name="criar_noticia"),
    path("logout/", views.logout, name="logout")
]