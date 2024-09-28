from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateProduct
from .models import Products
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError
from brand.models import Brands

# Create your views here.
# Display all products list to normal view
def productsListView(request):
    try:
        data = Products.objects.all()
        return render(request, 'products/list.html', { 'products' : data, 'title' : 'List of All Products' })
    except IntegrityError:
        return HttpResponse("Integrity error occured")
    except DatabaseError:
        return HttpResponse("Database error occured")

def productsListByBrandView(request, slug):
    try:
        data = Products.objects.filter(barndName=slug)
        brandName = Brands.objects.get(id=slug).brandName
        return render(request, 'products/list.html', { 'products' : data, 'title' : f'List of {brandName} brand\'s Products' })
    except IntegrityError:
        return HttpResponse("Integrity error occured")
    except DatabaseError:
        return HttpResponse("Database error occured")
    except ObjectDoesNotExist:
        return HttpResponse("Object not found")

#detailed product view in normal view
def productDetailView(request, slug):
    try:
        data = Products.objects.all()[:5] #getting 5 products data
        datum = Products.objects.get(id=slug)
        return render(request, 'products/product-details.html', { 'product' : datum, 'products' : data })
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
        