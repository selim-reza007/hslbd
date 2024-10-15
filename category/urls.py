from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('add-category', views.addCategoryView, name="add-category"),
]
