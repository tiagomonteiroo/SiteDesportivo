from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("login/", views.auth_login, name = "login"),
    path("loja/", views.loja, name = "loja"),
    path("bilhetes/", views.bilhetes, name = "bilhetes"),
    path("criarbilhete/", views.criar_bilhete, name="criarbilhete"),
    path("noticias/", views.ultimas_noticias, name = "noticias"),
    path("clube/", views.clube, name = "clube"),
    path("socio/", views.socio, name = "socio"),
    path("plantel/", views.plantel, name="plantel"),
    path("registar/", views.criar_utilizador, name="registar"),
    path("criarnoticia/", views.criar_noticia, name="criar_noticia"),
    path("criarproduto/", views.criar_produto, name="criar-produto"),
    path("eliminarproduto/", views.eliminar_produto, name="eliminar-produto"),
    path("eliminarnoticia/", views.eliminar_noticia, name="eliminar_noticia"),
    path("eliminarjogo/", views.eliminar_jogo, name="eliminar_jogo"),
    path("eliminarjogador/", views.eliminar_jogador, name="eliminar_jogador"),
    path("eliminartreinador/", views.eliminar_treinador, name="eliminar_treinador"),
    path("criarjogo/", views.criar_jogo, name="criar_jogo"),
    path("criarjogador/", views.criar_jogador, name="criar_jogador"),
    path("criartreinador/", views.criar_treinador, name="criar_treinador"),
    path("logout/", views.logout, name="logout"),
    path("tornasocio/", views.torna_socio, name="tornasocio"),
    path("deixasocio/", views.deixa_socio, name="deixasocio"),
    path("carrinho/", views.carrinho, name="carrinho"),
    path("adicionarcarrinho/<int:product_id>/", views.adicionar_carrinho, name='adicionarcarrinho'),
    path("removercarrinho/<int:product_id>/", views.remover_do_carrinho, name='removercarrinho'),
    path("checkout/", views.checkout, name='checkout')
]