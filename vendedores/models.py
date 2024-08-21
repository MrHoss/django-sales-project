from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    comissao = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
