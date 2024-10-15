from django import forms
from products.models import Category

class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryName', 'slug', 'typeTitle')
    