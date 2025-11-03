from django.urls import path, include
from shop.views import CategoryViewSet, ProductViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('api/', include(router.urls))
]