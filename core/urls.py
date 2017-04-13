from django.conf.urls import url
from .views import product_list, category , product

urlpatterns = [


    url(r'produtos/$', product_list, name='product_list'),
    url(r'produto/(?P<slug>[\w_-]+)$', product, name='product'),
    url(r'categoria/(?P<slug>[\w_-]+)', category,  name='category'),

]