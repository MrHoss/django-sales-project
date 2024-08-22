from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendaViewSet

app_name = 'vendas'

router = DefaultRouter()
router.register(r'vendas', VendaViewSet, basename='vendas')

urlpatterns = [
    path('', include(router.urls)),
]
