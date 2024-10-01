from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('', views.aboutUsView, name='aboutus'), #loads simple static content to normat view
    path('dashboard/add/', views.createAboutUsView, name='add-info'), #loads form to dashboard for create new profile info
    path('dashboard/edit/<int:id>/', views.updateAboutUsView, name='edit-info'), #Edit about us info
]
