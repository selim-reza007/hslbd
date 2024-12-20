from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.shortcuts import render
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, { 'document_root' : settings.MEDIA_ROOT }),
    re_path(r'^static/(?P<path>.*)$', serve, { 'document_root' : settings.STATIC_ROOT }),
    path('super/admin/user/', admin.site.urls),
    path('', views.homeView, name='home'),  # Loads home page
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('products/', include('products.urls')),
    path('gallery/', include('gallery.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('contactus/', include('contactus.urls')),
    path('brand/', include('brand.urls')),
    path('admin/', include('user.urls')),
    path('category/', include('category.urls')),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def custom_404_view(request, exception=None):
    return render(request, 'Not-found.html', status=404)

handler404 = custom_404_view