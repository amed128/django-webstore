from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE) # put 'Collection' in case the function is underneath
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True)
    inventory = models.IntegerField()

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title
    

class Message(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    review = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    # pass

    def __str__(self):
        return self.review





