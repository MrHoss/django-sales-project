from django.test import TestCase
from .models import ItemVenda
from vendas.models import Venda
from produtos.models import Produto, GrupoProduto
from clientes.models import Cliente
from vendedores.models import Vendedor

class ItemVendaTestCase(TestCase):
    def setUp(self):
        grupo = GrupoProduto.objects.create(nome="Eletrônicos")
        produto = Produto.objects.create(nome="Smartphone", preco=1200.00, grupo=grupo)
        cliente = Cliente.objects.create(nome="Bruno", email="bruno@example.com")
        vendedor = Vendedor.objects.create(nome="Paula", email="paula@example.com", comissao=8.00)
        venda = Venda.objects.create(cliente=cliente, vendedor=vendedor, total=1200.00)
        ItemVenda.objects.create(venda=venda, produto=produto, quantidade=1, preco=1200.00)

    def test_item_venda_criado(self):
        item = ItemVenda.objects.get(produto__nome="Smartphone")
        self.assertEqual(item.quantidade, 1)
        self.assertEqual(item.preco, 1200.00)
