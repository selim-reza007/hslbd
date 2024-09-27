from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CreateCompanyProfile
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import CompanyInfo

# Create your views here.
#used to render about us form in normal view
def aboutUsView(request):
    return render(request, 'aboutus/aboutus.html')

def createAboutUsView(request):
    if request.method == "POST":
        form = CreateCompanyProfile(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Company profile added.")
                return redirect('dashboard')
            except IntegrityError:
                return HttpResponse("Integrity error occured.")
            except DatabaseError:
                return HttpResponse("Database error occcured.")
    else:
        form = CreateCompanyProfile()
    return render(request, 'aboutus/dashboard/create.html', { 'form' : form})

def updateAboutUsView(request, slug):
    obj = get_object_or_404(CompanyInfo, id=slug)
    if request.method == "POST":
        form = CreateCompanyProfile(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Company profile updated.")
                return redirect('dashboard')
            except IntegrityError:
                return HttpResponse("Integrity error occured.")
            except DatabaseError:
                return HttpResponse("Database error occcured.")
    else:
        form = CreateCompanyProfile(instance=obj)
    return render(request, 'aboutus/dashboard/create.html', { 'form' : form})