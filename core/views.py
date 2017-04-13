from django.shortcuts import render

# Create your views here.
from core.models import Product, Category


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'produtos.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'produto.html', context)


def category(request, slug):
    current_category = Category.objects.get(slug=slug)
    product_list = Product.objects.filter(category__name=current_category.name)
    context = {
        'current_category': current_category,
        'product_list': product_list
    }
    return render(request, 'categoria.html', context)
