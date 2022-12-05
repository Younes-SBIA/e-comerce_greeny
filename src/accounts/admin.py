from django.contrib import admin

from .models import Profile, UserAddress, UserPhoneNumber

admin.site.register(Profile)
admin.site.register(UserAddress)
admin.site.register(UserPhoneNumber)
