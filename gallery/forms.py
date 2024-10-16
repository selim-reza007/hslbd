from django import forms
from .models import Gallery

max_size =  1 * 1024 * 1024  # 1MB
allowed_extensions = ['jpeg', 'jpg', 'png']  # List of allowed extensions

class AddImage(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']
        labels = {
            'image' : 'Upload Image',
        }
    
    def clean_image(self):
        file = self.cleaned_data.get('image')

        print("File result : ", file)

        if not file:
            raise forms.ValidationError("Please select an image to upload.")

        if file:
            if file.size > max_size:
                raise forms.ValidationError("File size shuold be less than 1MB.")
        
        extension = file.name.split('.')[-1].lower()
        if extension not in allowed_extensions:
            raise forms.ValidationError("Invalid file extension. Valid extensions are jpeg, jpg, png")
        return file