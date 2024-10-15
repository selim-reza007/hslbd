from django.shortcuts import render

# Create your views here.
def addCategoryView(request):
    return render(request, 'dashboard/add-category.html')