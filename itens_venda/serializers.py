from rest_framework import serializers
from .models import ItemVenda
from produtos.models import Produto

class ItemVendaSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco']
        extra_kwargs = {
            'preco': {'required': False}  # Preço não é necessário na criação
        }
