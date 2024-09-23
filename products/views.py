from django.shortcuts import render

# Create your views here.
def productsListView(request):
    return render(request, 'products/list.html')

def aoSmithProductsView(request):
    return render(request, 'products/ao-smith-products.html')

def philipsProductsView(request):
    return render(request, 'products/philips-products.html')

def productDetailView(request):
    return render(request, 'products/product-details.html')

#dashboard's views
def addNewProductView(request):
    return render(request, 'products/dashboard/add-product.html')