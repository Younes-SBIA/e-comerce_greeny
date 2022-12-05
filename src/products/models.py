from itertools import product
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.db.models.aggregates import Avg




class ProductManager(models.Manager):
    def price_greater_than(self, price):
        return self.filter(price__gt=price)
    
    def price_range(self, start,end):
        return self.filter(price__range=(start,end))


class Product(models.Model):

    PRODUCT_FLAG = (
        ("New", "New"),
        ("Feature","Feature"),
        ("Sale", "Sale")
    )

    # thin views , fat models

    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("sku"))
    subtitle = models.CharField(_("Subtitle"), max_length=300)
    desc = models.TextField(_("Description"), max_length=10000)
    flag = models.CharField(_("Flag"), max_length=10, choices=PRODUCT_FLAG)
    price = models.FloatField(_("Price"))
    image = models.ImageField(_("Image"), upload_to = 'product')
    tags = TaggableManager()
    category = models.ForeignKey("Category", verbose_name=_("Category"), related_name="product_category", on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey("Brand", verbose_name=_("Brand"), related_name="product_brand", on_delete=models.SET_NULL, blank=True, null=True)
    video_url = models.URLField(null=True, blank=True, verbose_name=_("Video"))
    quantity = models.IntegerField(default=50)
    
    objects = ProductManager()


    def __str__(self):
        return self.name
    
    def get_avg(self):
        avg = self.product_review.aggregate(myavg=Avg( "rate"))
        return avg 

    def get_avg2(self):
        rate_sum = 0
        product_review = self.product_review.all()
        for review in product_review:
            rate_sum += review.rate
            
        avg = rate_sum / len(product_review)

        return avg
class ProductImages(models.Model):

    product = models.ForeignKey(Product,verbose_name=_("Product"), related_name="product_images", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("Image"),upload_to="productsimages")
    
    def __str__(self):
        return str(self.product)



class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to="category")
    
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to="brand")
    
    def __str__(self):
        return self.name


class ProductReview(models.Model):
    user = models.ForeignKey(User,related_name="user_reviews", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product,verbose_name=_("Product"), on_delete=models.SET_NULL,null=True,blank=True, related_name="product_reviews")
    rate =models.ImageField(verbose_name=_("Rate"))
    created_ad = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return str(self.product)
    
    