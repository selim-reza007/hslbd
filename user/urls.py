from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('', views.loginView, name='user-login'),
    path('logout/', views.logoutView, name='user-logout'),
    path('change-password/', 
         auth_views.PasswordChangeView.as_view(template_name='user/change_password.html', success_url=reverse_lazy('user:password_change_done')), name='change_password'),
    path('change-password/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='user/change_password_done.html'), name='password_change_done'),
]