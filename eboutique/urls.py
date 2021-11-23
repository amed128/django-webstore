from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('collections/<str:pk>', views.collection, name="collection"),
    path('product/<str:pk>', views.product, name="product"),
    path('create-review/', views.createReview, name="create-review"),
    path('update-review/<str:pk>', views.updateReview, name="update-review"),
    path('delete-review/<str:pk>', views.deleteReview, name="delete-review"),
    
]

