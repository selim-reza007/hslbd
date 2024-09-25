from django.shortcuts import render, redirect, HttpResponse, get_list_or_404
from .forms import AddImage
from .models import Gallery
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError

# Create your views here
#pulling data from database to display in normal view
def galleryView(request):
    try:
        data = Gallery.objects.all()
    except IntegrityError:
        return HttpResponse("Integrity error occured.")
    except DatabaseError:
        return HttpResponse("Database error occured.")
    return render(request, 'gallery/gallery.html', { 'images' : data })

#pulling data from database to display in dashboard view
def dashboardGalleryView(request):
    try:
        data = Gallery.objects.all()
    except IntegrityError:
        return HttpResponse("Integrity error occured.")
    except DatabaseError:
        return HttpResponse("Database error occured.")
    return render(request, 'gallery/dashboard/gallery.html', { 'images' : data })

# add image
def addNewImageView(request):
    if request.method == "POST":
        form = AddImage(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('gallary:dasboard-gallery')
        except IntegrityError:
            return HttpResponse("Integrity error occured.")
        except DatabaseError:
            return HttpResponse("Database error occured.")
    else:
        form = AddImage()
    return render(request, 'gallery/dashboard/add-image.html', { 'form' : form })

# edit image
def editImageView(request, slug):
    item = Gallery.objects.get(id=slug)
    if request.method == "POST":
        form = AddImage(request.POST, request.FILES, instance=item)
        try:
            if form.is_valid():
                form.save()
                return redirect('gallary:dasboard-gallery')
        except IntegrityError:
            return HttpResponse("Integrity error occured.")
        except DatabaseError:
            return HttpResponse("Database error occured.")
    form = AddImage(instance=item)
    return render(request, 'gallery/dashboard/add-image.html', { 'form' : form })

#delete image
def deleteImageView(request, slug):
    if request.method == "POST":
        item = get_list_or_404(Gallery ,id=slug)
        if item:
            item.delete()
            return redirect('gallary:dasboard-gallery')