from rest_framework import viewsets
from .models import Venda
from .serializers import VendaBaseSerializer, VendaDetailSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return VendaDetailSerializer
        return VendaBaseSerializer
