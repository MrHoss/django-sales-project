from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendedorViewSet

app_name = 'vendedores'

# Criação do router
router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet, basename='vendedores')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
