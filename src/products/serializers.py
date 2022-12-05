from dataclasses import fields
from rest_framework import serializers
from .models import Product, Category, Brand, ProductReview



class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model  = Product
    # fields = ['id', 'name',  "sku", "subtitle", "desc",'flag', "price", "image", "quantity", "video_url",'brand', 'category']
    fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
  class Meta:
    model  = Category
    fields = "__all__"
    

class CategoryDetailSerializer(serializers.ModelSerializer):
  products = ProductSerializer(source="product_category", many=True)
  class Meta:
    model  = Category
    fields = ["id", "name", "image", "products"]


class BrandListSerializer(serializers.ModelSerializer):
  class Meta:
    model  = Brand
    fields = "__all__"


class BrandDetailSerializer(serializers.ModelSerializer):
  products = ProductSerializer(source="product_brand", many=True)
  class Meta:
    model  = Brand
    fields = ["id", "name", "image", "products"]
    


class ProductReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductReview
    fields = ["user", "product", "rate", "review"]
    
    


class ProductDetailSerializer(serializers.ModelSerializer):
  reviews = ProductReviewSerializer(source="product_reviews", many=True)
  class Meta:
    model  = Product
    fields = ['id', 'name',  "sku", "subtitle", "desc",'flag', "price", "image", "quantity", "video_url",'brand', 'category', 'reviews']
    # fields = "__all__"