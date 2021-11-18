from django.contrib import admin

# Register your models here.
from . models import Collection, Product, Brand, Message

admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Message)