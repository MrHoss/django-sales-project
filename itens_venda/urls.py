from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemVendaViewSet

router = DefaultRouter()
router.register(r'itens-venda', ItemVendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
