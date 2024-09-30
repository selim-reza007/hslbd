from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CreateCompanyProfile
from django.db import IntegrityError, DatabaseError, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import CompanyInfo
from django.contrib.auth.decorators import login_required

# Create your views here.
#used to render about us form in normal view
def aboutUsView(request):
    return render(request, 'aboutus/aboutus.html')

#Create form for adding aboutus info. Will only be render if there is no data already created.
@login_required(login_url='/admin/')
def createAboutUsView(request):
    if request.method == "POST":
        form = CreateCompanyProfile(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    messages.success(request, "Company profile added.")
                    return redirect('dashboard')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = CreateCompanyProfile()
    return render(request, 'aboutus/dashboard/create.html', { 'form' : form})

@login_required(login_url='/admin/')
def updateAboutUsView(request, slug):
    obj = get_object_or_404(CompanyInfo, id=slug)
    if request.method == "POST":
        form = CreateCompanyProfile(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    messages.success(request, "Company profile updated.")
                    return redirect('dashboard')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = CreateCompanyProfile(instance=obj)
    return render(request, 'aboutus/dashboard/create.html', { 'form' : form})