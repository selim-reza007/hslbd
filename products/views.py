from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError
from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateProduct
from .models import Products

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
def productDashboardView(request):
    try:
        data = Products.objects.all()
        return render(request, 'products/dashboard/list-porduct.html', { 'products' : data })
    except ObjectDoesNotExist:
        return HttpResponse("Item not found", status=404)
    except IntegrityError:
        return HttpResponse("Integrity error occurred", status=40)
    except DatabaseError:
        return HttpResponse("Database error occurred", status=500)

def addNewProductView(request):
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('products:list-product')
        except ObjectDoesNotExist:
            return HttpResponse("Item not found", status=404)
        except IntegrityError:
            return HttpResponse("Integrity error occurred", status=400)
        except DatabaseError:
            return HttpResponse("Database error occurred", status=500)
    else:
        form = CreateProduct()
        return render(request, 'products/dashboard/add-product.html', { 'form' : form })
