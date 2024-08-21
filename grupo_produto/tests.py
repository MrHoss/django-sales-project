from django.test import TestCase
from .models import GrupoProduto

class GrupoProdutoTestCase(TestCase):
    def setUp(self):
        GrupoProduto.objects.create(nome="Eletrônicos")

    def test_grupo_produto_criado(self):
        grupo = GrupoProduto.objects.get(nome="Eletrônicos")
        self.assertEqual(grupo.nome, "Eletrônicos")
