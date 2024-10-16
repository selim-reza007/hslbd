from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import CreateCategory
from django.db import IntegrityError
from products.models import Category
from django.contrib import messages

# Create your views here.

#listing out all created categories
def allCategoriesView(request):
    data = Category.objects.all()
    return render(request, 'dashboard/all-category.html', { 'categories' : data })

#Creating new category
def addCategoryView(request):
    if request.method == "POST":
        form = CreateCategory(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "New Category added successfully")
                return redirect('category:all-categories')
            except ImportError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
    else:
        form = CreateCategory()
    return render(request, 'dashboard/add-category.html', { 'form' : form })


#edit category
def editCategoryView(request, slug):
    datum = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        form = CreateCategory(request.POST, instance=datum)
        if form.is_valid:
            try:
                form.save()
                return redirect('category:all-categories')
            except ImportError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
    else:
        form = CreateCategory(instance=datum)
    return render(request, 'dashboard/add-category.html', { 'form' : form })