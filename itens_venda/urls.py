from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemVendaViewSet

app_name = 'itens_venda'

# Criação do router
router = DefaultRouter()
router.register(r'itens_venda', ItemVendaViewSet, basename='itens_venda')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
