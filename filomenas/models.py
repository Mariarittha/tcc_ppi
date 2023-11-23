from operator import mod
from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.FloatField()
    imagem = models.ImageField()
    descricao_produto = models.CharField(max_length=1000)

class hospede(models.Model):
    nome = models.CharField(max_length=120)
    profissao = models.CharField(max_length=120)
    email = models.CharField(max_length=150)
    idade = models.IntegerField()

class filomenas(models.Model):
    nome = models.CharField(max_length=120)
    idade = models.IntegerField()
    descricao = models.CharField(max_length=1000)

class estadia(models.Model):
    duracao = models.IntegerField()
    nome_estadia = models.CharField(max_length=200)
    descricao_estadia = models.CharField(max_length=1000)
    localizacao = models.CharField(max_length=500)
    valor = models.DecimalField(verbose_name=("valor"), decimal_places=2, max_digits=6)
    programacao = models.CharField(max_length=100)

