from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateProduct
from .models import Products
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError

# Create your views here.
def productsListView(request):
    return render(request, 'products/list.html')

def aoSmithProductsView(request):
    return render(request, 'products/ao-smith-products.html')

def philipsProductsView(request):
    return render(request, 'products/philips-products.html')

def productDetailView(request, slug):
    try:
        datum = Products.objects.get(id=slug)
        return render(request, 'products/product-details.html', { 'product' : datum })
    except ObjectDoesNotExist:
        return HttpResponse('Item not found', status=404)
    except IntegrityError:
        return HttpResponse('Integrity error occured', status=40)
    except DatabaseError:
        return HttpResponse('Database error occured', status=500)

#dashboard's views

#Viewing product info from dashboard
def productDetailDashboardView(request, slug):
    try:
        datum = Products.objects.get(id=slug)
        return render(request, 'products/dashboard/product-details.html', { 'product' : datum })
    except ObjectDoesNotExist:
        return HttpResponse('Item not found', status=404)
    except IntegrityError:
        return HttpResponse('Integrity error occured', status=40)
    except DatabaseError:
        return HttpResponse('Database error occured', status=500)

#Viewing products list from dashboard
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

#Creating new product
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
            return HttpResponse("Integrity error occurred", status=40)
        except DatabaseError:
            return HttpResponse("Database error occurred", status=500)
    else:
        form = CreateProduct()
        return render(request, 'products/dashboard/add-product.html', { 'form' : form })

#edting exissting product
def editProductView(request, slug):
    obj = Products.objects.get(id=slug)
    form = CreateProduct(instance=obj)
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES, instance=obj)
        try:
            if form.is_valid():
                form.save()
                return redirect('products:list-product')
        except ObjectDoesNotExist:
            return HttpResponse("Item not found", status=404)
        except IntegrityError:
            return HttpResponse("Integrity error occured", status=40)
        except DatabaseError:
            return HttpResponse("Database error", status=500)
    else:
        return render(request, 'products/dashboard/add-product.html', { 'form' : form })
    
#delete product
def deleteProductView(request, slug):
    if request.method == "POST":
        try:
            obj = Products.objects.get(id=slug)
            if obj:
                obj.delete()
                messages.success(request, f"{obj.productName} deleted successfully.")
                return redirect('products:list-product')
            else:
                return HttpResponse("Product not found.")
        except ObjectDoesNotExist:
            return HttpResponse("Item not found", status=404)
        except IntegrityError:
            return HttpResponse("Integrity error occured", status=40)
        except DatabaseError:
            return HttpResponse("Database error", status=500)
        