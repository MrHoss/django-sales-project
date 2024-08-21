from django.db import models
from clientes.models import Cliente
from vendedores.models import Vendedor

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    data_venda = models.DateField()

    def __str__(self):
        return f"Venda {self.id} - {self.cliente} - {self.data_venda}"

    @property
    def total(self):
        from itens_venda.models import ItemVenda
        return sum(item.preco * item.quantidade for item in ItemVenda.objects.filter(venda=self))
