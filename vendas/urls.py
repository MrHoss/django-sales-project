from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendaViewSet

app_name = 'vendas'

# Criação do router
router = DefaultRouter()
router.register(r'vendas', VendaViewSet, basename='vendas')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
