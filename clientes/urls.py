from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

app_name = 'clientes'

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls)),
]
