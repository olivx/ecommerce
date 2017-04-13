from django.db import models
from django.shortcuts import resolve_url

# Create your models here.

class Category(models.Model):

    name = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Identificador',max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.CharField('Identificador', max_length=100)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, verbose_name='Categoria')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('ecommerce:product' , slug=self.slug)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
