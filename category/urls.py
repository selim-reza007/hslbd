from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('dashboard/all-categories', views.allCategoriesView, name="all-categories"),
    path('dashboard/add-category', views.addCategoryView, name="add-category"),
    path('dashboard/edit-category/<slug:slug>', views.editCategoryView, name="edit-category"),
    path('dashboard/delete-category/<slug:slug>', views.deleteCategoryView, name="delete-category"),
]
