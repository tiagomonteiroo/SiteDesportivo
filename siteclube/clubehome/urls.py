from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("plantel/", views.plantel, name = "plantel" ),
    path ("loja/", views.loja, name = "loja")
]