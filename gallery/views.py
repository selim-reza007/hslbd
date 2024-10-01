from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import AddImage
from .models import Gallery
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here
#pulling data from database to display in normal view
def galleryView(request):
    try:
        data = Gallery.objects.all()
    except IntegrityError:
        return HttpResponse("Integrity error occurred.")
    except DatabaseError:
        return HttpResponse("Database error occurred.")
    return render(request, 'gallery/gallery.html', { 'images' : data })

#pulling data from database to display in dashboard view
@login_required(login_url='/admin/')
def dashboardGalleryView(request):
    try:
        data = Gallery.objects.all()
    except IntegrityError:
        return HttpResponse("Integrity error occurred.")
    except DatabaseError:
        return HttpResponse("Database error occurred.")
    return render(request, 'gallery/dashboard/gallery.html', { 'images' : data })

# add image
@login_required(login_url='/admin/')
def addNewImageView(request):
    if request.method == "POST":
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('gallary:dasboard-gallery')
            except IntegrityError:
                return HttpResponse("Integrity error occurred.")
            except DatabaseError:
                return HttpResponse("Database error occurred.")
    else:
        form = AddImage()
    return render(request, 'gallery/dashboard/add-image.html', { 'form' : form })

# edit image
@login_required(login_url='/admin/')
def editImageView(request, slug):
    item = Gallery.objects.get(id=slug)
    if request.method == "POST":
        form = AddImage(request.POST, request.FILES, instance=item)
        if form.is_valid():
            try:
                form.save()
                return redirect('gallary:dasboard-gallery')
            except IntegrityError:
                return HttpResponse("Integrity error occurred.")
            except DatabaseError:
                return HttpResponse("Database error occurred.")
    else:
        form = AddImage(instance=item)
    return render(request, 'gallery/dashboard/add-image.html', { 'form' : form })

#delete image
@login_required(login_url='/admin/')
def deleteImageView(request, slug):
    if request.method == "POST":
        item = get_object_or_404(Gallery ,id=slug)
        if item:
            try:
                item.delete()
                messages.success(request,"The Image has been deleted successfully!")
                return redirect('gallary:dasboard-gallery')
            except IntegrityError:
                return HttpResponse("Integrity error occurred.")
            except DatabaseError:
                return HttpResponse("Database error occurred.")