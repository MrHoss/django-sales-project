import django_filters
from .models import Venda

class VendaFilter(django_filters.FilterSet):
    class Meta:
        model = Venda
        fields = {
            'data': ['exact', 'gte', 'lte'],  # Filtrar por data exata, maior ou menor
            'vendedor': ['exact'],            # Filtrar por vendedor
            'cliente': ['exact'],             # Filtrar por cliente
        }
