from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^produto/$', TemplateView.as_view(template_name='produto.html'), name='produto'),
    url(r'^produtos/$', TemplateView.as_view(template_name='produtos.html'), name='produtos'),
    url(r'^contato/$', TemplateView.as_view(template_name='contato.html'), name='contato'),

]
