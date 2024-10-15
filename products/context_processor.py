from .models import Type

def productsType(request):
    types = Type.objects.all()
    return { 'typeItems' : types }