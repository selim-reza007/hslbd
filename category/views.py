from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateCategory
from django.db import IntegrityError, DatabaseError

# Create your views here.
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