from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from . models import Collection, Product, Message, Brand
from client.models import Order
from . forms import ReviewForm

# create your views here
# def index(request):
#     return HttpResponse("Hello from eBoutique")

def index(request):
    now = datetime.now

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    products = Product.objects.filter(
        Q(collection__name__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(brand__name__icontains=q)
    )
    products = products.order_by('title')
    collections = Collection.objects.all().order_by('name')
    brands = Brand.objects.all().order_by('name')

    try:
        order = Order.objects.get(customer=request.user.customer, completed=False)
    except:
        order = {}

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { "now": now, 
                # "products": products, 
                "collections": collections, 
                "brands":brands, 
                "q":q, 
                "order": order,
                "page_obj": page_obj
            }
    return render(request, "eboutique/home.html", context)

def collection(request, pk):
    pass

def product(request, pk):
    product = Product.objects.get(id=pk)
    product_messages = product.message_set.all().order_by('-created')      #get all the kids related to that parent
    comments_count = product_messages.count()

    try:
        order = Order.objects.get(customer=request.user.customer, completed=False)
    except:
        order = {}

    #To add a review
    if request.method == 'POST':
        message = Message.objects.create(
            host=request.user,
            product=product,
            review=request.POST.get('body')
        )
        return redirect('product', pk=product.id)

    context = { "product": product,
                "product_messages": product_messages, 
                "comments_count":comments_count,
                "order":order
                }
    return render(request, "eboutique/product.html", context)

def createReview(request):
    pass

def updateReview(request, pk):
    message = Message.objects.get(id=pk)
    product = message.product
    form = ReviewForm(instance=message)
    # next = request.POST.get('next', '/')
    if request.method ==  'POST':
        form = ReviewForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('product', pk=product.id)
    context = {"form": form}
    return render(request, 'eboutique/reviewPage.html', context) 

def deleteReview(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('index')
    return render(request, 'eboutique/delete.html', {}) 