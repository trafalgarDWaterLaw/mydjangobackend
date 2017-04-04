from django.contrib import admin

# Register your models here.
from models import users,products

admin.site.register(users)
admin.site.register(products)