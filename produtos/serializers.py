# produtos/serializers.py
from rest_framework import serializers
from .models import Produto
from grupo_produto.models import GrupoProduto

class ProdutoSerializer(serializers.ModelSerializer):
    grupo = serializers.PrimaryKeyRelatedField(
        queryset=GrupoProduto.objects.all(),
        help_text="Escolha um grupo de produto."
    )

    class Meta:
        model = Produto
        fields = '__all__'
