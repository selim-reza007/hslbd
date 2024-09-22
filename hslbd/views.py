from django.shortcuts import render
from contactus.views import unreadMsgCount

def homeView(request):
    return render(request, 'index.html')

def dashboardView(request):
    number = unreadMsgCount(request)
    return render(request, 'my_admin/dashboard.html', { 'count' : number })