from django.urls import path
from . import views

app_name = 'gallary'

urlpatterns = [
    path('', views.galleryView, name='gallary'), #loads image gallery in normal view
    path('dashboard/gallery/', views.dashboardGalleryView, name='dasboard-gallery'), #loads image gallery in dashboard
    path('dashboard/add-image', views.addNewImageView, name='add-image'), #add image
    path('dashboard/update-image/<int:id>/', views.editImageView, name='edit-image'), #change image
    path('dashboard/delete-image/<int:id>/', views.deleteImageView, name='delete-image'), #delete existing image
]
