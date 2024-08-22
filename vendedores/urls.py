from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendedorViewSet

app_name = 'vendedores'

router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet, basename='vendedores')

urlpatterns = [
    path('', include(router.urls)),
]
