from django.test import TestCase
from .models import Produto, GrupoProduto

class ProdutoTestCase(TestCase):
    def setUp(self):
        grupo = GrupoProduto.objects.create(nome="Eletrônicos")
        Produto.objects.create(nome="Notebook", preco=2500.00, grupo=grupo)

    def test_produto_criado(self):
        produto = Produto.objects.get(nome="Notebook")
        self.assertEqual(produto.preco, 2500.00)
        self.assertEqual(produto.grupo.nome, "Eletrônicos")
