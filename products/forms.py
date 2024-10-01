from django import forms
from .models import Products

max_size = 1 * 1024 * 1024
allowed_extension = ['jpeg', 'jpg', 'png']

class CreateProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['productName','barndName', 'info1', 'info2', 'info3', 'info4', 'info5', 'info6', 'info7', 'info8', 'info9', 'info10', 'info11', 'info12', 'info13', 'info14', 'info15', 'description', 'productImage']
        labels = {
            'productName' : 'Product Name',
            'barndName' : 'Brand Name',
            'info1' : 'Information field 1',
            'info2' : 'Information field 2',
            'info3' : 'Information field 3',
            'info4' : 'Information field 4',
            'info5' : 'Information field 5',
            'info6' : 'Information field 6',
            'info7' : 'Information field 7',
            'info8' : 'Information field 8',
            'info9' : 'Information field 9',
            'info10' : 'Information field 10',
            'info11' : 'Information field 11',
            'info12' : 'Information field 12',
            'info13' : 'Information field 13',
            'info14' : 'Information field 14',
            'info15' : 'Information field 15',
            'description' : 'Description',
            'productImage' : 'Product Image'
        }

        def clean_productImage(self):
            file = self.cleaned_data.get('productImage')

            # If no file is uploaded and no image exists in the instance, let the model's default handle it
            if not file:
                return None  # This will use the model's default 'fallback.jpg' if the image field is left blank

            # Validate file if uploaded
            if file:
                # Check file size
                if file.size > max_size:
                    raise forms.ValidationError("File size should be less than 1MB")

            # Check file extension
            extension = file.name.split('.')[-1].lower()
            if extension not in allowed_extension:
                raise forms.ValidationError("Not allowed file format. Allowed formats are jpeg, jpg, png")

            return file