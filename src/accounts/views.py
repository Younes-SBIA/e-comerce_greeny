from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .forms import SignupForm , UserActivateForm
from .models import Profile , UserAddress , UserPhoneNumber
from django.contrib.auth.models import User
from products import models as product_models
from orders import models as orders_models
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save()
            
            profile = Profile.objects.get(user__username=username)
            profile.active = False 
            profile.save()
            
            # send email 
            send_mail(
                subject="Activate Your Account" , 
                message=f"use this code {profile.code} to activate your account",
                from_email = "younessbia31@gmail.com",
                recipient_list= [email] , 
                fail_silently=False
            )
            return redirect(f'/accounts/{username}/activate')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})



def user_activte(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code :
                profile.activate = True
                profile.code = ''
                profile.code_used = True
                return redirect('/accounts/login')
        
    else:
        form = UserActivateForm()
    return render(request,'registration/activation.html',{'form':form})




def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_address = UserAddress.objects.filter(user=request.user)
    phone_numbers = UserPhoneNumber.objects.filter(user=request.user)
    
    return render(request,'registration/profile.html',{'profile':profile , 'user_address':user_address ,'phone_numbers':phone_numbers })


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    users = User.objects.all().count()
    products = product_models.Product.objects.all().count()
    orders = orders_models.Order.objects.all().count()
    reviews = product_models.ProductReview.objects.all().count()
    category = product_models.Category.objects.all().count()
    brand = product_models.Brand.objects.all().count()
    
    
    receieved_order = orders_models.Order.objects.filter(status='receieved').count()
    processed_order = orders_models.Order.objects.filter(status='processed').count()
    shiped_order = orders_models.Order.objects.filter(status='shiped').count()
    delivered_order = orders_models.Order.objects.filter(status='delivered').count()
    
    return render(request,'accounts/dashboard.html',{
        'users': users , 
        'products': products, 
        'orders': orders,
        'reviews': reviews , 
        'category' : category , 
        'brand': brand , 
        'receieved_order': receieved_order , 
        'processed_order': processed_order , 
        'shiped_order': shiped_order, 
        'delivered_order': delivered_order
    })


from .tasks import print_welcome

def test_celery(reqeust):
    print_welcome.delay(20)