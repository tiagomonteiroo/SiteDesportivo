from django.contrib.auth.models import User
from django.db import models

class Plantel(models.Model):
    SIGLA_CHOICES = (
        ("A", "A"),
        ("B", "B")
    )
    sigla = models.CharField(max_length=1, choices=SIGLA_CHOICES)
    desporto = models.CharField(max_length=20)

class Jogador(models.Model):
    POSICAO_CHOICES = (
        ("Avançado", "Avançado"),
        ("Extremo", "Extremo"),
        ("Médio", "Médio"),
        ("Central", "Central"),
        ("Lateral", "Lateral"),
        ("Guarda-Redes", "Guarda-Redes")
    )
    numero = models.IntegerField()
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=20, choices=POSICAO_CHOICES)
    idade = models.IntegerField()
    plantel = models.ForeignKey(Plantel, on_delete=models.CASCADE)

class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    idade = models.IntegerField()
    plantel = models.ForeignKey(Plantel, on_delete=models.CASCADE)

class Principal(Treinador):
    pass

class Auxiliar(Treinador):
    pass


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100, default="Produto")

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_socio = models.BooleanField(default=False)
    NIF = models.IntegerField(default=0)

class Bilhete(Produto):
    data = models.DateField()
    lugar = models.IntegerField()
    N_Emissao = models.IntegerField()

class Venda(models.Model):
    utilizador = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
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