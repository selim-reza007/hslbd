from django.urls import path
from . import views

app_name = 'contactus'

urlpatterns = [
    path('', views.contactUsView, name='contactus'), #loads contactus page
    path('dashboard/messages/', views.requestedMsgView, name='requested-msg'), #loads all request message in dashboard
    path('dashboard/messages/details/<slug:slug>/', views.messageDetailsView, name='details-msg'), #loads details of message in dashboard
    path('dashboard/messages/count-unread/', views.unreadMsgCount, name='unread-count'), #count number of unread messages
    path('dashboard/messages/update-status/', views.updateMsgStatus, name='update-status'), #update the status of message
    path('dashboard/messages/delete/<slug:slug>/', views.deleteMsg, name='delete-msg'), #delete requested message
]
