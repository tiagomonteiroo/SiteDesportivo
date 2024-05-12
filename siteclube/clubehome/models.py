import os.path

from django.contrib.auth.models import User
from django.db import models


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_socio = models.BooleanField(default=False)
    NIF = models.IntegerField(default=0)

class Noticia(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='clubehome/static/', null=True, blank=True)
    imagem_nome = models.CharField(max_length=255, null=True, blank=True)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_news_count = Noticia.objects.count()
            filename = f'noticia{existing_news_count + 1}.png'
            self.imagem.name = os.path.join('noticias', filename)
            self.imagem_nome = filename
        super().save(*args, **kwargs)


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

class Product(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, default='Produto')
    imagem = models.ImageField(upload_to='clubehome/static/', null=True, blank=True)
    imagem_nome = models.CharField(max_length=255, null=True, blank=True)
    preco = models.IntegerField(default=0)
    cod_produto = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_products_count = Product.objects.count()
            filename = f'produto{existing_products_count + 1}.png'
            self.imagem.name = os.path.join('imagens', filename)
            self.imagem_nome = filename
        super().save(*args, **kwargs)

class Carrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Product, through="ItemCarrinho")

class ItemCarrinho (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField(default=1)

class Venda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Product)

class Bilhete (Product):
    equipa_fora=models.CharField(max_length=255)
    equipa_casa=models.CharField(max_length=255)
    data= models.DateField()

