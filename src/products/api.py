# view api

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from products.MyPagination import MyPagination
from products.filters import ProductFilter
from products.models import Brand, Category, Product, ProductReview
from products.serializers import ProductSerializer, CategoryListSerializer, CategoryDetailSerializer,BrandListSerializer, BrandDetailSerializer, ProductDetailSerializer
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend




class ProductListAPI(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  pagination_class = MyPagination
  filter_backends = [DjangoFilterBackend]
  filterset_class = ProductFilter
  filterset_fields = ['name', 'subtitle','price','quantity']
  search_fields = ['name', 'subtitle']
  
  # permission_classes = [IsAuthenticated]
  
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductDetailSerializer
  
  
  
  
  
class CategorylistAPI(generics.ListAPIView):
  serializer_class = CategoryListSerializer
  queryset = Category.objects.all()
  
class CategoryDetailAPI(generics.RetrieveAPIView):
  queryset = Category.objects.all()
  serializer_class = CategoryDetailSerializer
  
  
  
class BrandlistAPI(generics.ListAPIView):
  serializer_class = BrandListSerializer
  queryset = Brand.objects.all()
  
class BrandDetailAPI(generics.RetrieveAPIView):
  queryset = Brand.objects.all()
  serializer_class = BrandDetailSerializer