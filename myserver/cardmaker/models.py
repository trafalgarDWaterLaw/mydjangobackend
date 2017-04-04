from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, default='', unique=True)
    user_id = models.AutoField(primary_key=True)
    email_id = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)

class products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    productname = models.CharField(max_length=100, default='', unique=True)
    #image_url = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100, default='')
    premium = models.BooleanField(default = False)
    user_id = models.ForeignKey(users,to_field='user_id')
    user_upload = models.BooleanField(default= False)
    layout = models.CharField(max_length=100, blank=True)