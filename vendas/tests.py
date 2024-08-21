from django.test import TestCase
from .models import Venda
from clientes.models import Cliente
from vendedores.models import Vendedor

class VendaTestCase(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(nome="Carlos", email="carlos@example.com")
        vendedor = Vendedor.objects.create(nome="Ana", email="ana@example.com", comissao=5.00)
        Venda.objects.create(cliente=cliente, vendedor=vendedor, total=300.00)

    def test_venda_criada(self):
        venda = Venda.objects.get(cliente__nome="Carlos")
        self.assertEqual(venda.total, 300.00)
        self.assertEqual(venda.vendedor.nome, "Ana")
