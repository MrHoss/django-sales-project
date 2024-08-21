from rest_framework import serializers
from vendas.models import Venda  # Importar modelo de vendas ou outro necessário

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
