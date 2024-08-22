from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoProdutoViewSet

app_name = 'grupo_produto'

# Criação do router
router = DefaultRouter()
router.register(r'grupo_produto', GrupoProdutoViewSet, basename='grupo_produto')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
