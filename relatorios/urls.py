from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelatorioViewSet

app_name = 'relatorios'

# Criação do router
router = DefaultRouter()
router.register(r'relatorios', RelatorioViewSet, basename='relatorios')

urlpatterns = [
    # Inclui todas as rotas definidas pelo router
    path('', include(router.urls)),
]
