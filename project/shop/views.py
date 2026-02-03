from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.models import Category, Product
from shop.serializers import CategorySerializer,ProductSerializer
 
class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()
    
class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
# class ArticleViewSet(ReadOnlyModelViewSet):
#     serializer_class = ArticleSerializer
#     def get_queryset(self):
#         return Article.objects.filter(active=True) 