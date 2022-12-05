from django.urls import path 
from .views import signup, user_activte, profile, test_celery,dashboard

app_name = "accounts"

urlpatterns = [
  path('dashboard/', dashboard, name='dashboard'),
  path('test-celery/', test_celery),
  path('signup' , signup , name='signup'),
  path('profile/' , profile , name='profile'),
  path('<str:username>/activate' , user_activte , name='user_activate')
]