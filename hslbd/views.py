from django.shortcuts import render

def homeView(request):
    return render(request, 'index.html')

def dashboardView(request):
    return render(request, 'my_admin/dashboard.html')