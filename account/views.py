from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from client.models import Order
from . forms import UserForm

def registerUser(request):
    page = 'Registration'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error occured')
    
    context = {'form':form, 'page': page}
    return render(request, 'account/register_login.html', context)

def loginUser(request):
    page = 'Login'
    if request.user.is_authenticated:
        return redirect('index')
    
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            Order.objects.get_or_create(customer=request.user.customer, completed=False)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password incorrect')
    except:
        messages.error(request, 'User does not exist')
    
    context = {'page':page}
    return render(request, 'account/register_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')
