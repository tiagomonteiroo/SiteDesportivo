from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("plantel/", views.plantel, name = "plantel"),
    path("loja/", views.loja, name = "loja"),
    path("bilhetes/", views.bilhetes, name = "bilhetes"),
    path("noticias/", views.noticias, name = "noticias"),
    path("resultados/", views.resultados, name = "resultados"),
    path("clube/", views.clube, name = "clube"),
    path("socio/", views.socio, name = "socio")
]