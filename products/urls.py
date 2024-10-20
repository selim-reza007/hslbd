from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('all/<slug:slug>', views.productsListView, name="all-products"),#display all products in normal view
    path('all/category/<int:categoryId>', views.loadsProductsByCategoryNormalView, name='category-products'), #listing products based on category in normal view
    path('dashboard/list/', views.productDashboardView, name='list-product'), #Listing all Products in Dashboard
    path('dashboard/by-type/<int:typeId>', views.loadsProductsBtTypeView, name="products-by-type"), #listing all product based on Type in dashboard
    path('dashboard/by-category/<int:categoryId>', views.loadsProductsBtCategoryView, name='products-by-category'), #listing all product based on Category in dashboard
    path('dashboard/add/<int:typeId>', views.addNewProductView, name='add-product'), #adding product
    path('dashboard/types/', views.loadAllTypesView, name='load-types'), #listing all types to dashboard
    path('<int:id>/list/', views.productsListByBrandView, name='by-brand'), #display products by brand
    path('details/<int:id>/', views.productDetailView, name='details'), #details info in Normal view
    path('dashboard/edit/<int:id>/', views.editProductView, name='edit'), #edting product
    path('dashboard/details/<int:id>/', views.productDetailDashboardView,name='dashboard-details'), #details product in dashboard
    path('dashboard/delete/<int:id>/', views.deleteProductView, name='delete'), #delete product
]
