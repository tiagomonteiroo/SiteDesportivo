from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("login/", views.auth_login, name = "login"),
    path("noticias/", views.ultimas_quatro, name = "noticias"),
    path("clube/", views.clube, name = "clube"),
    path("socio/", views.socio, name = "socio"),
    path("plantel/", views.plantel, name="plantel"),
    path("registar/", views.criar_utilizador, name="registar"),
    path("criarnoticia/", views.criar_noticia, name="criar_noticia"),
    path("criarjogo/", views.criar_jogo, name="criar_jogo"),
    path("logout/", views.logout, name="logout"),
    path("loja/", views.loja, name="loja"),
    path("criarproduto/", views.criar_produto, name="criar-produto")
]