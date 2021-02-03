from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=255)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    stockQtd = models.IntegerField('Quantidade em Estoque')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Nome', max_length=255)
    lastName = models.CharField('Sobrenome', max_length=255, default='')
    email = models.EmailField('E-mail', max_length=255, unique=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name
