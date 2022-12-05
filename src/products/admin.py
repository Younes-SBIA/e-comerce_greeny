from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, ProductImages, ProductReview, Category, Brand

# Register your models here.

class ProductImagesInLine(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ["name", "price", 'flag']
    inlines= [ProductImagesInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Category)
admin.site.register(Brand)