from django.shortcuts import render
from contactus.views import unreadMsgCount
from products.models import Products

def homeView(request):
    data = Products.objects.all()[:3]
    return render(request, 'index.html', { 'products' : data })

def dashboardView(request):
    number = unreadMsgCount(request)
    return render(request, 'my_admin/dashboard.html', { 'count' : number })