from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelatorioViewSet

app_name = 'relatorios'

router = DefaultRouter()
router.register(r'relatorios', RelatorioViewSet, basename='relatorios')

urlpatterns = [
    path('', include(router.urls)),
]
