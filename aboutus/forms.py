from django import forms
from .models import CompanyInfo

# Constants
max_size = 5 * 1024 * 1024  # 5MB
allowed_extensions = ['pdf']  # List of allowed extensions

class CreateCompanyProfile(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = ['mobile', 'email', 'profile']

    def clean_profile(self):
        file = self.cleaned_data.get('profile')

        if not file:
            return None

        if file:
            # File size validation
            if file.size > max_size:
                raise forms.ValidationError("File size exceeds the allowed limit of 5MB.")
            
            # File extension validation
            extension = file.name.split('.')[-1].lower()
            if extension not in allowed_extensions:
                raise forms.ValidationError("Invalid file extension. Only PDF file is allowed.")

        return file
