from django.shortcuts import render

# Create your views here.
#used to render about us form in normal view
def aboutUsView(request):
    return render(request, 'aboutus/aboutus.html')