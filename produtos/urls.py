from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

app_name = 'produtos'

# Criação do router
router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produtos')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
