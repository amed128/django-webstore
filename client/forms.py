# from django import forms
# from django.db.models import fields
from django.forms import ModelForm
from .models import ShippingAddress

class ShippingForm(ModelForm):
    class Meta:
        model = ShippingAddress
        # fields = '__all__'
        fields = ['firstname', 'lastname', 'address', 'city', 'state', 'zipcode']