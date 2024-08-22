from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('clientes/', views.clientes, name='clientes'),
    path('grupo_produto/', views.grupo_produto, name='grupo_produto'),
    path('itens_venda/', views.itens_venda, name='itens_venda'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('vendas/', views.vendas, name='vendas'),
    path('sobre/', views.sobre, name='sobre'),
    path('vendedores/', views.vendedores, name='vendedores'),
]
