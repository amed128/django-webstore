from eboutique.models import Product
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    firtname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    orderdate = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False) 

    def __str__(self):
        order_title = str(self.customer) + '-' + str(self.orderdate)
        return order_title

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(default=0, null=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    # address_complement = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.PositiveSmallIntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)