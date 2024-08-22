from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemVendaViewSet

app_name = 'itens_venda'

router = DefaultRouter()
router.register(r'itens_venda', ItemVendaViewSet, basename='itens_venda')

urlpatterns = [
    path('', include(router.urls)),
]
