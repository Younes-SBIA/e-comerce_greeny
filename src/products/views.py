from itertools import product
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# from products.forms import ProductReviewForm
from .models import Product, ProductImages, Brand, Category
from django.db.models import Count, Q, F, Value
from django.db.models.functions import Concat
from django.db.models.aggregates import Min, Max, Sum, Avg, Count


"""
def post_list(request):
    # objects = Product.objects.all()
    # objects = Product.objects.filter(price__range=(30,50))
    # objects = Product.objects.filter(category__id=10)
    # objects = Product.objects.filter(category__id__gt=10)
    # objects = Product.objects.filter(name__contains="Miranda")
    # objects = Product.objects.filter(name__startswith="Mi")
    # objects = Product.objects.filter(name__endswith="m")
    # objects = Product.objects.filter(desc__isnull=True)
    # objects = Product.objects.filter(desc__isnull=False)
    # objects = Product.objects.filter(quantity__gt=10)
    # objects = Product.objects.filter(quantity__gt=10, price__gt=50)
    
    # objects = Product.objects.filter(
    #     Q(quantity__gt=10) |
    #     Q(price__gt=50)
    #     )
    
    # objects = Product.objects.filter(
    #     Q(quantity__gt=10) &
    #     Q(price__gt=50)
    #     )
    
    # objects = Product.objects.filter(
    #     Q(quantity__gt=10) &
    #     ~Q(price__gt=50)
    #     )
    
    # objects = Product.objects.filter(quantity=F("price"))
    # objects = Product.objects.filter(quantity=F("category__id"))
    # objects = Product.objects.order_by("name")
    # objects = Product.objects.order_by("-name")  # - => (6) not − => clavier numériques
    # objects = Product.objects.order_by("name", "-price")
    # objects = Product.objects.filter(quantity=F("price")).order_by("name")
    # objects = Product.objects.all().order_by("-name")[:10]
    # objects = Product.objects.earliest("name")
    # objects = Product.objects.latest("name")
    # print(objects)
    # objects = Product.objects.all()[:10]
    # objects = Product.objects.all()[10:20]
    # objects = Product.objects.values('id', 'name','category__name')
    # objects = Product.objects.values_list('id', 'name','category__name')
    # objects = Product.objects.only('id', 'name')
    # objects = Product.objects.select_related('category').all()   #one-to-one relationship , foreignkey
    # objects = Product.objects.prefetch_related('category').all()   #one-to-many relationship , foreignkey
    # objects = Product.objects.annotate(is_new=Value(True))
    '''  objects = Product.objects.annotate(
        full_name = Concat("name", Value(' '),"flag")
    ) '''
    # objects = Product.objects.aggregate(Count("id"))
    # objects = Product.objects.aggregate(Sum("price"))
    # objects = Product.objects.aggregate(Sum("price"), Max("price"))
    # objects = Product.objects.price_greater_than(40)
    objects = Product.objects.price_range(40, 60)
    
    print(objects)
    
    
    return render(request, 'products/test_list.html', {'products': objects})
"""

# from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(60)
def post_list(request):
    objects = Product.objects.all()    
    return render(request, 'products/test_list.html', {'products': objects})


class ProductList(ListView):
    model = Product
    paginate_by = 10
    
class ProductDetail(DetailView):
    model= Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context["related"] = Product.objects.filter(category=myproduct.category)
        return context
    

class BrandList(ListView):
    model = Brand
    # paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context
    

class BrandDetail(DetailView):
    model =  Brand
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand =  self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    

class CategoryList(ListView):
    model = Category
    # paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all().annotate(product_count=Count('product_category')) 
        return context
    
    class CategoryDetail(DetailView):
        model = Category
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            category = self.get_object()
            context["category_products"] = Product.objects.filter(category=category)
            return context
    
    
    
# from django.http import JsonResponse
# from django.template.loader import render_to_string

# def add_review(request,id):
#     product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductReviewForm(request.POST)
#         if form.is_valid():
#             myform = form.save(commit=False)
#             myform.product = product
#             myform.user = request.user
#             myform.save()
            
#             reviews = ProductReview.objects.filter(product=product)
#             html = render_to_string('include/review.html',{'reviews':reviews, request:request})
#             return JsonResponse({'result':html})
