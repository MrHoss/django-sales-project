from django.test import TestCase
from .models import Vendedor

class VendedorTestCase(TestCase):
    def setUp(self):
        Vendedor.objects.create(nome="Maria", email="maria@example.com", comissao=10.00)

    def test_vendedor_criado(self):
        vendedor = Vendedor.objects.get(nome="Maria")
        self.assertEqual(vendedor.email, "maria@example.com")
        self.assertEqual(vendedor.comissao, 10.00)
