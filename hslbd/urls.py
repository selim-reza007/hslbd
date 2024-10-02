from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('super/admin/', admin.site.urls),
    path('', views.homeView, name='home'),  # Loads home page
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('products/', include('products.urls')),
    path('gallery/', include('gallery.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('contactus/', include('contactus.urls')),
    path('brand/', include('brand.urls')),
    path('admin/', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)