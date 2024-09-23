from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('all/', views.productsListView, name="all-products"),
    path('brand/ao-smith/', views.aoSmithProductsView, name="ao-smith"),
    path('brand/philips/', views.philipsProductsView, name="philips"),
    path('details/', views.productDetailView, name="details"),
    path('dashboard/list/', views.productDashboardView, name='list-product'),
    path('dashboard/add/', views.addNewProductView, name='add-product'),
]
