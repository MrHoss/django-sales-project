# vendas/serializers.py
from rest_framework import serializers
from .models import Venda
from itens_venda.models import ItemVenda
from itens_venda.serializers import ItemVendaSerializer

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'vendedor', 'data_venda', 'itens', 'total']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens', [])
        venda = Venda.objects.create(**validated_data)
        for item_data in itens_data:
            ItemVenda.objects.create(venda=venda, **item_data)
        return venda

    def update(self, instance, validated_data):
        itens_data = validated_data.pop('itens', [])
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.vendedor = validated_data.get('vendedor', instance.vendedor)
        instance.data_venda = validated_data.get('data_venda', instance.data_venda)
        instance.save()

        # Atualiza ou cria os itens vendidos
        for item_data in itens_data:
            item_id = item_data.get('id')
            if item_id:
                item = ItemVenda.objects.get(id=item_id, venda=instance)
                item.produto = item_data.get('produto', item.produto)
                item.quantidade = item_data.get('quantidade', item.quantidade)
                # O preço será atualizado automaticamente pelo método save() do modelo
                item.save()
            else:
                ItemVenda.objects.create(venda=instance, **item_data)
        return instance

    def get_total(self, obj):
        return sum(item.preco * item.quantidade for item in obj.itens.all())
