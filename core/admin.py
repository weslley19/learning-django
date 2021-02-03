from django.contrib import admin
from .models import Product, Client


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'stockQtd', 'created', 'updated')


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('name', 'lastName', 'email', 'created', 'updated')
