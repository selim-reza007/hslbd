from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateCategory
from django.db import IntegrityError, DatabaseError
from products.models import Category
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
                return HttpResponse("New product category added")
            except ImportError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = CreateCategory()
    return render(request, 'dashboard/add-category.html', { 'form' : form })