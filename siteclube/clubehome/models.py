import os.path

from django.contrib.auth.models import User
from django.db import models


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_socio = models.BooleanField(default=False)
    NIF = models.IntegerField(default=0)


class Venda(models.Model):
    utilizador = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

class Noticia(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='clubehome/static/noticias/')
    data_publicacao = models.DateField(auto_now_add=True)


class Jogo(models.Model):
    adversario = models.CharField(max_length=50)
    golos_clube = models.PositiveIntegerField()
    golos_adversario = models.PositiveIntegerField()
    local = models.CharField(max_length=10, choices=[('fora', 'Fora'), ('casa', 'Casa')])
    data_jogo = models.DateField()

class Player(models.Model):
    POSITION_CHOICES = (
        ("Avançado", "Avançado"),
        ("Extremo", "Extremo"),
        ("Médio", "Médio"),
        ("Central", "Central"),
        ("Lateral", "Lateral"),
        ("Guarda-Redes", "Guarda-Redes")
    )
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    age = models.IntegerField()

class Coach(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    age = models.IntegerField()
    main = models.BooleanField(default=True)