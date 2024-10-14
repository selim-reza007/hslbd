from django.shortcuts import render
from contactus.views import unreadMsgCount
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError

def homeView(request):
    data = Products.objects.all()[:3]
    print("Products data: ",data)
    return render(request, 'index.html', { 'products' : data })

@login_required(login_url='/admin/')
def dashboardView(request):
    number = unreadMsgCount(request)
    return render(request, 'my_admin/dashboard.html', { 'count' : number })