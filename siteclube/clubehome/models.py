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

class Conta(models.Model):
    email = models.EmailField()
    palavra_passe = models.CharField(max_length=100)

class Utilizador(Conta):
    nome = models.CharField(max_length=100)
    NIF = models.IntegerField()
    nascimento = models.DateField()

class Admin(Conta):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    ano_entrada = models.DateField()

class Socio(Utilizador):
    N_Socio = models.IntegerField()
    is_socio = models.BooleanField()

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ID_prod = models.IntegerField()

class Venda(models.Model):
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()

class Bilhete(Produto):
    data = models.DateField()
    lugar = models.IntegerField()
    N_Emissao = models.IntegerField()

class Merchandising(Produto):
    tipo = models.CharField(max_length=100)

