from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoProdutoViewSet

router = DefaultRouter()
router.register(r'grupo_produto', GrupoProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
