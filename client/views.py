from django.http.response import JsonResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from eboutique.models import Product
from .models import Customer, Order, OrderItem, ShippingAddress
from .forms import ShippingForm
import json


# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        try:
            # customer = Customer.objects.get(user=request.user) 
            customer = request.user.customer        
        except:
            customer = Customer.objects.create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()

    else:
        items = []

    context = {'items':items, 'customer':customer, 'order':order}
    return render(request, 'client/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        try:
            # customer = Customer.objects.get(user=request.user) 
            customer = request.user.customer        
        except:
            customer = Customer.objects.create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()

    else:
        items = []

    
    try:
        shippingaddress = ShippingAddress.objects.get(customer=request.user.customer)
        form = ShippingForm(instance=shippingaddress)
    except:
        shippingaddress = None
        form = ShippingForm()

    if request.method ==  'POST':
        if shippingaddress:
            return redirect('cart')
        else:
            shippingaddress = ShippingAddress.objects.create(
                customer = request.user.customer,
                order = order,
                firstname = request.POST.get('firstname'),
                lastname = request.POST.get('lastname'),
                address = request.POST.get('address'),
                city = request.POST.get('city'),
                state = request.POST.get('state'),
                zipcode = request.POST.get('zipcode')
            )
            return redirect('cart')


    context = {'items':items, 'customer':customer, 'order':order, "form": form}
    return render(request, 'client/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
    orderitem.save()

    if orderitem.quantity <= 0 or action == 'delete':
        orderitem.delete()
    
    return JsonResponse('Item was added', safe=False)


    