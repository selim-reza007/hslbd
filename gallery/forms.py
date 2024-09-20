from django import forms
from .models import Gallery

class AddImage(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']
        labels = {
            'image' : 'Upload Image',
        }