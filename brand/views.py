from django.shortcuts import render, redirect, get_list_or_404, HttpResponse
from .forms import CreateBrand
from .models import Brands
from django.db import IntegrityError, DatabaseError

# Create your views here.
def brandsListView(request):
    try:
        data = Brands.objects.all()
    except IntegrityError:
        return HttpResponse("Integrity error occured")
    except DatabaseError:
        return HttpResponse("Database error occured")
    return render(request, 'brand/dashboard/list.html', { 'brands' : data })

# create new brand
def createBrandView(request):
    form = CreateBrand()
    if request.method == "POST":
        form = CreateBrand(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('brand:brand-list')
        except IntegrityError:
            return HttpResponse("Integrity error occured")
        except DatabaseError:
            return HttpResponse("Database error occured")
    return render(request, 'brand/dashboard/create.html', { 'form' : form })

# update brand
def editBrandView(request, slug):
    obj = get_list_or_404(Brands ,id=slug)
    if request.method == "POST":
        form = CreateBrand(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                return redirect('brand:brand-list')
        except IntegrityError:
            return HttpResponse("Integrity error occured")
        except DatabaseError:
            return HttpResponse("Database error occured")
    else:
        form = CreateBrand(instance=obj)
        return render(request,'brand/dashboard/create.html', { 'form' : form })

#delete brand item
def deleteBrandView(request, slug):
    if request.method == "POST":
        obj = get_list_or_404(id=slug)
        obj.delete()
        return redirect('brand:brand-list')