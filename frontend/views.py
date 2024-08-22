from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def produtos(request):
    return render(request, 'frontend/produtos.html')

def clientes(request):
    return render(request, 'frontend/clientes.html')

def grupo_produto(request):
    return render(request, 'frontend/grupo_produto.html')

def itens_venda(request):
    return render(request, 'frontend/itens_venda.html')

def relatorios(request):
    return render(request, 'frontend/relatorios.html')

def vendas(request):
    return render(request, 'frontend/vendas.html')

def sobre(request):
    return render(request, 'frontend/sobre.html')

def vendedores(request):
    return render(request, 'frontend/vendedores.html')
