from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.loginView, name='user-login'),
    path('logout/', views.logoutView, name='user-logout'),
]