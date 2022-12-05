from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Company(models.Model):

    name = models.CharField(_('Name'), max_length=100)
    logo = models.ImageField(_('Logo'), upload_to='company/')
    subtitle = models.CharField(_('Subtitle'), max_length=500)
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    ins_link = models.URLField(null=True, blank=True)
    address = models.TextField(_('Address'), max_length=200)
    phone_nomber = models.TextField(_('Phone'), max_length=200)
    email = models.TextField(_('Email'), max_length=200)
    call_us = models.TextField(_('Call us'), max_length=25)
    email_us = models.EmailField(_('Email us'))
    
    
    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companys")

    def __str__(self):
        return self.name


