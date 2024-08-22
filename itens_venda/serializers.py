from rest_framework import serializers
from .models import ItemVenda
from produtos.serializers import ProdutoSerializer

class ItemVendaSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco']
