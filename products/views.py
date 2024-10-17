from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CreateProduct
from .models import Products
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError
from brand.models import Brands
from django.contrib.auth.decorators import login_required
from .models import Type, Category

# Create your views here.
# Display all products list to normal view
def productsListView(request):
    try:
        data = Products.objects.all().order_by('-id')
        return render(request, 'products/list.html', { 'products' : data, 'title' : 'List of All Products' })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

#display products list by brand in normal view
def productsListByBrandView(request, id):
    try:
        data = Products.objects.filter(barndName=id)
        brandName = Brands.objects.get(id=id).brandName
        return render(request, 'products/list.html', { 'products' : data, 'title' : f'List of {brandName} brand\'s Products' })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    except ObjectDoesNotExist:
        return render(request, 'Error.html', { 'errorMsg' : 'Objects not found!' })

#detailed product view in normal view
def productDetailView(request, id):
    try:
        data = Products.objects.all()[:5] #getting 5 products data
        datum = get_object_or_404(Products, id=id)
        return render(request, 'products/product-details.html', { 'product' : datum, 'products' : data })
    except ObjectDoesNotExist:
        return render(request, 'Error.html', { 'errorMsg' : 'Object not found!' })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

#dashboard's views
#Viewing product info from dashboard
@login_required(login_url='/admin/')
def productDetailDashboardView(request, id):
    datum = get_object_or_404(Products, id=id)
    return render(request, 'products/dashboard/product-details.html', { 'product' : datum })

#Viewing products list from dashboard
@login_required(login_url='/admin/')
def productDashboardView(request):
    evenNumbers = [1,3,5,7,9,11,13,15]
    try:
        data = Products.objects.all().order_by('-id')
        types = Type.objects.all()
        return render(request, 'products/dashboard/list-porduct.html', { 'products' : data, 'types' : types, 'evens' : evenNumbers })
    except ObjectDoesNotExist:
        return render(request, 'Error.html', { 'errorMsg' : 'Item not found!' })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

#Creating new product in Dashboard
@login_required(login_url='/admin/')
def addNewProductView(request, typeId):
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES, typeTitle=typeId)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "New product information is added successfully")
                return redirect('products:list-product')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
    else:
        form = CreateProduct(typeTitle=typeId)
    return render(request, 'products/dashboard/add-product.html', { 'form' : form})

#edting exissting product
@login_required(login_url='/admin/')
def editProductView(request, id):
    obj = get_object_or_404(Products, id=id)
    categoryObj = Category.objects.get(id=obj.categoryTitle.id)
    typeId = categoryObj.typeTitle.id
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES, typeTitle=typeId, instance=obj)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"{obj.productName}'s data is updated!")
                return redirect('products:list-product')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = CreateProduct(typeTitle=typeId, instance=obj)
    return render(request, 'products/dashboard/add-product.html', { 'form' : form })
    
#delete product
@login_required(login_url='/admin/')
def deleteProductView(request, id):
    if request.method == "POST":
        obj = get_object_or_404(Products, id=id)
        if obj:
            try:
                obj.delete()
                messages.success(request, f"{obj.productName} deleted successfully.")
                return redirect('products:list-product')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
        else:
            return HttpResponse("Product not found.")
        

#added after 16th october 2024

#loads types to dashboard's for creaing product
def loadAllTypesView(request):
    types = Type.objects.all()
    evenNumbers = [1,3,5,7,9,11,13,15]
    return render(request, 'products/dashboard/select-type.html', { 'types' : types, 'evens' : evenNumbers })

#display Products by Type
def loadsProductsBtTypeView(request):
    return render(request, 'products/dashboard/products-by-type.html')