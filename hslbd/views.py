from django.shortcuts import render
from contactus.views import unreadMsgCount
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError

def homeView(request):
    try:
        data = Products.objects.all()[:3]
        return render(request, 'index.html', { 'products' : data })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

@login_required(login_url='/admin/')
def dashboardView(request):
    number = unreadMsgCount(request)
    return render(request, 'my_admin/dashboard.html', { 'count' : number })