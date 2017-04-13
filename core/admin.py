from django.contrib import admin

from core.models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'slug' , 'created','modified',)
    list_filter = ('created', 'modified',)
    search_fields = ('name', 'slug',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug' , 'category','price',)
    list_filter = ('category','created',)
    search_fields = ('name', 'slug', 'category__name')

    prepopulated_fields = {'slug': ('name',)}