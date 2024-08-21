from django.test import TestCase
from .models import Cliente

class ClienteTestCase(TestCase):
    def setUp(self):
        Cliente.objects.create(nome="João", email="joao@example.com", telefone="123456789", endereco="Rua A")

    def test_cliente_criado(self):
        cliente = Cliente.objects.get(nome="João")
        self.assertEqual(cliente.email, "joao@example.com")
        self.assertEqual(cliente.telefone, "123456789")
        self.assertEqual(cliente.endereco, "Rua A")
