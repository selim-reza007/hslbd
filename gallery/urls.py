from django.urls import path
from . import views

app_name = 'gallary'

urlpatterns = [
    path('', views.galleryView, name='gallary'),
    path('dashboard/gallery/', views.dashboardGalleryView, name='dasboard-gallery'),
    path('dashboard/add-image', views.addNewImageView, name='add-image'),
    path('dashboard/update-image/<slug:slug>/', views.editImageView, name='edit-image'),
    path('dashboard/delete-image/<slug:slug>/', views.deleteImageView, name='delete-image'),
]
