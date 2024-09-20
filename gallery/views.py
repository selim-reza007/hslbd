from django.shortcuts import render, redirect
from .forms import AddImage
from .models import Gallery

# Create your views here.
def galleryView(request):
    data = Gallery.objects.all()
    return render(request, 'gallery/gallery.html', { 'images' : data })

def dashboardGalleryView(request):
    data = Gallery.objects.all()
    return render(request, 'gallery/dashboard/gallery.html', { 'images' : data })

def addNewImageView(request):
    if request.method == "POST":
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallary:dasboard-gallery')
    else:
        form = AddImage()
    return render(request, 'gallery/dashboard/add-image.html', { 'form' : form })

def editImageView(request, slug):
    item = Gallery.objects.get(id=slug)
    if request.method == "POST":
        form = AddImage(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('gallary:dasboard-gallery')
    form = AddImage(instance=item)
    return render(request, 'gallery/dashboard/add-image.html', { 'form' : form })

def deleteImageView(request, slug):
    if request.method == "POST":
        item = Gallery.objects.get(id=slug)
        if item:
            item.delete()
            return redirect('gallary:dasboard-gallery')