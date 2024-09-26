from django import template
from brand.models import Brands


register = template.Library()

# Define the inclusion tag
@register.inclusion_tag('components/_brands_category.html')
def show_brands():
    brands = Brands.objects.all()  # Fetch all brands from the database
    return {'brands': brands}     # Pass the brands to the template
