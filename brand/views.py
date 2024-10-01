from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CreateBrand
from .models import Brands
from django.db import IntegrityError, DatabaseError
from django.contrib.auth.decorators import login_required

# Create your views here.
#listing all brand info to dashboard view
@login_required(login_url='/admin/')
def brandsListView(request):
    try:
        data = Brands.objects.all()
        return render(request, 'brand/dashboard/list.html', { 'brands' : data })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

# create new brand
@login_required(login_url='/admin/')
def createBrandView(request):
    if request.method == "POST":
        form = CreateBrand(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('brand:brand-list')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = CreateBrand()
    return render(request, 'brand/dashboard/create.html', { 'form' : form })

# update brand
@login_required(login_url='/admin/')
def editBrandView(request, id):
    obj = get_object_or_404(Brands ,id=id)
    if request.method == "POST":
        form = CreateBrand(request.POST, instance=obj)
        if form.is_valid():
            try:
                form.save()
                return redirect('brand:brand-list')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = CreateBrand(instance=obj)
    return render(request,'brand/dashboard/create.html', { 'form' : form })

#delete brand item
@login_required(login_url='/admin/')
def deleteBrandView(request, id):
    if request.method == "POST":
        obj = get_object_or_404(Brands ,id=id)
        try:
            obj.delete()
            return redirect('brand:brand-list')
        except IntegrityError:
            return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
        except DatabaseError:
            return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })