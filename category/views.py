from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import CreateCategory
from django.db import IntegrityError, DatabaseError
from products.models import Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

#listing out all created categories
@login_required(login_url='/admin/')
def allCategoriesView(request):
    data = Category.objects.all()
    return render(request, 'category/dashboard/all-category.html', { 'categories' : data })

#Creating new category
@login_required(login_url='/admin/')
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
    return render(request, 'category/dashboard/add-category.html', { 'form' : form })


#edit category
@login_required(login_url='/admin/')
def editCategoryView(request, slug):
    datum = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        form = CreateCategory(request.POST, instance=datum)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, "Category updated.")
                return redirect('category:all-categories')
            except ImportError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
    else:
        form = CreateCategory(instance=datum)
    return render(request, 'category/dashboard/add-category.html', { 'form' : form })

#delete category
@login_required(login_url='/admin/')
def deleteCategoryView(request, slug):
    datum = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        try:
            datum.delete()
            messages.success(request, "Category Deleted.")
            return redirect('category:all-categories')
        except DatabaseError:
            return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })