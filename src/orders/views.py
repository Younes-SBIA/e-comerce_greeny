from urllib import request
from django.shortcuts import render
from orders.models import Cart, CartDetail

from products.models import Product



def add_to_cart(request):
  if request.method == 'POST':
    product_id = request.POST['product_id']
    quantity = request.POST['quantity']
    
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user, status="inprogress")
    
    cart_Detail,created = CartDetail.objects.get_or_create(
      cart = cart,
      product = product,
    )

    cart_Detail.quantity = quantity
    cart_Detail.price = product.price
    cart_Detail.total = int(quantity) * product.price
    cart_Detail.save()
