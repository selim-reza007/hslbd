from django import forms
from .models import Brands


class CreateBrand(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['brandName', 'country']
        labels = {
            'brandName' : 'Brand Name',
            'country' : 'Country',
        }
    