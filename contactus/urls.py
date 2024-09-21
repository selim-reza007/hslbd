from django.urls import path
from . import views

app_name = 'contactus'

urlpatterns = [
    path('', views.contactUsView, name='contactus'),
    path('messages/', views.requestedMsgView, name='requested-msg'),
    path('messages/details/', views.messageDetailsView, name='details-msg'),
]
