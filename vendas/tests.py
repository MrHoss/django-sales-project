from django.test import TestCase
from .models import Venda
from clientes.models import Cliente
from vendedores.models import Vendedor
from itens_venda.models import ItemVenda
from produtos.models import Produto, GrupoProduto

class VendaTestCase(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(nome="Carlos", email="carlos@example.com")
        vendedor = Vendedor.objects.create(nome="Ana", email="ana@example.com", comissao=5.00)

        grupo = GrupoProduto.objects.create(nome="Grupo1")

        produto1 = Produto.objects.create(nome="Produto1", preco=50.00, grupo=grupo)

        self.venda = Venda.objects.create(cliente=cliente, vendedor=vendedor, data_venda="2024-08-22")

        ItemVenda.objects.create(venda=self.venda, produto=produto1, quantidade=2, preco=produto1.preco)

    def test_venda_criada(self):
        venda = Venda.objects.get(cliente__nome="Carlos")
        self.assertEqual(venda.total, 100.00)  # Ajuste o valor esperado conforme o total correto
        self.assertEqual(venda.vendedor.nome, "Ana")
