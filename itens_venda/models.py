from django.db import models
from produtos.models import Produto

class ItemVenda(models.Model):
    venda = models.ForeignKey('vendas.Venda', related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', related_name='itens_venda', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.preco is None:
            self.preco = self.produto.preco
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unidades"
