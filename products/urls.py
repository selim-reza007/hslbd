from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('all/', views.productsListView, name="all-products"),#display all products in normal view
    path('dashboard/list/', views.productDashboardView, name='list-product'), #Listing all Products in Dashboard
    path('dashboard/add/', views.addNewProductView, name='add-product'), #adding product
    path('<slug:slug>/list/', views.productsListByBrandView, name='by-brand'), #display products by brand
    path('details/<slug:slug>/', views.productDetailView, name='details'), #details info in Normal view
    path('dashboard/edit/<slug:slug>/', views.editProductView, name='edit'), #edting product
    path('dashboard/details/<slug:slug>/', views.productDetailDashboardView,name='dashboard-details'), #details product in dashboard
    path('dashboard/delete/<slug:slug>/', views.deleteProductView, name='delete'), #delete product
]
