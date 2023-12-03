from django.db import models

from datetime import datetime
from django.db import models
from django.utils.safestring import mark_safe



class Categoria(models.Model):
    categoria = models.CharField(max_length=80)
    
    def __str__(self) -> str:
        return self.categoria


class Opcoes(models.Model):
    nome = models.CharField(max_length=40)
    acrescimo = models.FloatField(default=0)
    ativo = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.nome


class Adicional(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    maximo = models.IntegerField()
    minimo = models.IntegerField()
    opcoes = models.ManyToManyField(Opcoes)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome_produto = models.CharField(max_length=500)
    img = models.ImageField(upload_to='post_img')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    descricao = models.TextField()
    ingredientes = models.CharField(max_length=2000)
    adicionais = models.ManyToManyField(Adicional, blank=True)
    ativo = models.BooleanField(default=True)
    
    @mark_safe # renderiza tags html no lugar de campos que seriam strings
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'
    
    def __str__(self):
        return self.nome_produto