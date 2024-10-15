from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('dashboard/all-categories', views.allCategoriesView, name="all-categories"),
    path('dashboard/add-category', views.addCategoryView, name="add-category"),
]
