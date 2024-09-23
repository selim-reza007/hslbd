from django.shortcuts import render, redirect
from .forms import CreateBrand
from .models import Brands

# Create your views here.
def brandsListView(request):
    data = Brands.objects.all()
    return render(request, 'brand/dashboard/list.html', { 'brands' : data })

def createBrandView(request):
    form = CreateBrand()
    if request.method == "POST":
        form = CreateBrand(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand:brand-list')
    return render(request, 'brand/dashboard/create.html', { 'form' : form })

def editBrandView(request, slug):
    obj = Brands.objects.get(id=slug)
    if request.method == "POST":
        form = CreateBrand(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('brand:brand-list')
    else:
        form = CreateBrand(instance=obj)
        return render(request,'brand/dashboard/create.html', { 'form' : form })
    
def deleteBrandView(request, slug):
    if request.method == "POST":
        obj = Brands.objects.get(id=slug)
        obj.delete()
        return redirect('brand:brand-list')