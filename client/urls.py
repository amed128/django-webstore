from django.urls import path

from . import views  #from the current directory import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
]