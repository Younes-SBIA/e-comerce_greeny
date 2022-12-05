from django_filters import rest_framework
from .models import Product



class ProductFilter(rest_framework.FilterSet):
    class Meta:
        model = Product
        fields={
            'name' : ['icontains'],
            'subtitle': ['icontains'],
            'price':['lte','gte'],
            'quantity':['lte','gte'],
        }