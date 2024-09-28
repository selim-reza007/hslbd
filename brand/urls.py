from django.urls import path
from . import views

app_name = "brand"

#here all routes are been used to perform on brands in dashboard view.
urlpatterns = [
    path('dashboard/list/', views.brandsListView, name='brand-list'), #display all brands
    path('dashboard/add/', views.createBrandView, name='brand-add'), #Add brand
    path('dashboard/edit/<slug:slug>/', views.editBrandView, name='brand-edit'), #edit brand
    path('dashboard/delete/<slug:slug>/', views.deleteBrandView, name='brand-delete'), #delete brand
]
