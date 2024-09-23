from django.urls import path
from . import views

app_name = "brand"

urlpatterns = [
    path('dashboard/list/', views.brandsListView, name='brand-list'),
    path('dashboard/add/', views.createBrandView, name='brand-add'),
    path('dashboard/edit/<slug:slug>/', views.editBrandView, name='brand-edit'),
    path('dashboard/delete/<slug:slug>/', views.deleteBrandView, name='brand-delete'),
]
