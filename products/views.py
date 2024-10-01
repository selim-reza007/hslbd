from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CreateProduct
from .models import Products
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError
from brand.models import Brands
from django.contrib.auth.decorators import login_required

# Create your views here.
# Display all products list to normal view
def productsListView(request):
    try:
        data = Products.objects.all().order_by('-id')
        return render(request, 'products/list.html', { 'products' : data, 'title' : 'List of All Products' })
    except IntegrityError:
        return HttpResponse("Integrity error occurred")
    except DatabaseError:
        return HttpResponse("Database error occurred")

#display products list by brand in normal view
def productsListByBrandView(request, slug):
    try:
        data = Products.objects.filter(barndName=slug)
        brandName = Brands.objects.get(id=slug).brandName
        return render(request, 'products/list.html', { 'products' : data, 'title' : f'List of {brandName} brand\'s Products' })
    except IntegrityError:
        return HttpResponse("Integrity error occurred")
    except DatabaseError:
        return HttpResponse("Database error occurred")
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
        return HttpResponse('Integrity error occurred', status=40)
    except DatabaseError:
        return HttpResponse('Database error occurred', status=500)

#dashboard's views
#Viewing product info from dashboard
@login_required(login_url='/admin/')
def productDetailDashboardView(request, slug):
    try:
        datum = Products.objects.get(id=slug)
        return render(request, 'products/dashboard/product-details.html', { 'product' : datum })
    except ObjectDoesNotExist:
        return HttpResponse('Item not found', status=404)
    except IntegrityError:
        return HttpResponse('Integrity error occurred', status=40)
    except DatabaseError:
        return HttpResponse('Database error occurred', status=500)

#Viewing products list from dashboard
@login_required(login_url='/admin/')
def productDashboardView(request):
    try:
        data = Products.objects.all().order_by('-id')
        return render(request, 'products/dashboard/list-porduct.html', { 'products' : data })
    except ObjectDoesNotExist:
        return HttpResponse("Item not found", status=404)
    except IntegrityError:
        return HttpResponse("Integrity error occurred", status=40)
    except DatabaseError:
        return HttpResponse("Database error occurred", status=500)

#Creating new product in Dashboard
@login_required(login_url='/admin/')
def addNewProductView(request):
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "New product information is added successfully")
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
@login_required(login_url='/admin/')
def editProductView(request, slug):
    obj = Products.objects.get(id=slug)
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"{obj.productName}'s data is updated!")
                return redirect('products:list-product')
            except ObjectDoesNotExist:
                return HttpResponse("Item not found", status=404)
            except IntegrityError:
                return HttpResponse("Integrity error occurred", status=40)
            except DatabaseError:
                return HttpResponse("Database error", status=500)
    else:
        form = CreateProduct(instance=obj)
    return render(request, 'products/dashboard/add-product.html', { 'form' : form })
    
#delete product
@login_required(login_url='/admin/')
def deleteProductView(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Products, id=slug)
        if obj:
            try:
                obj.delete()
                messages.success(request, f"{obj.productName} deleted successfully.")
                return redirect('products:list-product')
            except ObjectDoesNotExist:
                return HttpResponse("Item not found", status=404)
            except IntegrityError:
                return HttpResponse("Integrity error occurred", status=40)
            except DatabaseError:
                return HttpResponse("Database error", status=500)
        else:
            return HttpResponse("Product not found.")