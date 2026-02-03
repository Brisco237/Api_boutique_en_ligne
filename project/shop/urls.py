from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', ProductViewSet, basename='products')
router.register('/category/', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]