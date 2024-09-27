from django import forms
from .models import CompanyInfo

class CreateCompanyProfile(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = ['mobile', 'email', 'profile']