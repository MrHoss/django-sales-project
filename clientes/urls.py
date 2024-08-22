from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

app_name = 'clientes'

# Criação do router
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='clientes')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
