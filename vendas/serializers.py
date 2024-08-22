from rest_framework import serializers
from .models import Venda
from clientes.models import Cliente
from vendedores.models import Vendedor
from itens_venda.models import ItemVenda
from itens_venda.serializers import ItemVendaSerializer
from clientes.serializers import ClienteSerializer
from vendedores.serializers import VendedorSerializer
from produtos.models import Produto

class VendaBaseSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    vendedor = serializers.PrimaryKeyRelatedField(queryset=Vendedor.objects.all())
    itens = serializers.ListField(
        child=serializers.DictField(),
        write_only=True
    )
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'vendedor', 'data_venda', 'itens', 'total']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens', [])
        venda = Venda.objects.create(**validated_data)
        for item_data in itens_data:
            produto = Produto.objects.get(id=item_data.pop('produto'))
            ItemVenda.objects.create(venda=venda, produto=produto, **item_data)
        return venda

    def update(self, instance, validated_data):
        itens_data = validated_data.pop('itens', [])
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.vendedor = validated_data.get('vendedor', instance.vendedor)
        instance.data_venda = validated_data.get('data_venda', instance.data_venda)
        instance.save()

        for item_data in itens_data:
            item_id = item_data.get('id')
            produto = Produto.objects.get(id=item_data.pop('produto'))
            if item_id:
                item = ItemVenda.objects.get(id=item_id, venda=instance)
                item.produto = produto
                item.quantidade = item_data.get('quantidade', item.quantidade)
                item.save()
            else:
                ItemVenda.objects.create(venda=instance, produto=produto, **item_data)
        return instance

    def get_total(self, obj):
        return sum(item.preco * item.quantidade for item in obj.itens.all())


class VendaDetailSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    vendedor = VendedorSerializer()
    itens = ItemVendaSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'vendedor', 'data_venda', 'itens', 'total']

    def get_total(self, obj):
        return sum(item.preco * item.quantidade for item in obj.itens.all())
