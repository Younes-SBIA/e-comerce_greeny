from django.urls import path
from products.views import ProductList, ProductDetail, BrandList, BrandDetail, CategoryList,post_list

from products.api import BrandDetailAPI, BrandlistAPI, ProductListAPI, ProductDetailAPI, CategorylistAPI, CategoryDetailAPI

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'products'


urlpatterns = [
    path("testing", post_list),
    path('', ProductList.as_view(), name='product_list'),
    path("<int:pk>", ProductDetail.as_view(), name='product_details'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path("brands/<int:pk>", BrandDetail.as_view(), name='brand_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),
    # path('category/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
    # api

    path("api/", ProductListAPI.as_view()),
    path("api/<int:pk>", ProductDetailAPI.as_view()),

    path("api/brands/", BrandlistAPI.as_view()),
    path("api/brands/<int:pk>", BrandDetailAPI.as_view()),

    path("api/category/", CategorylistAPI.as_view()),
    path("api/category/<int:pk>", CategoryDetailAPI.as_view()),
]

