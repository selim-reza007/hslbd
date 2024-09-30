from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                login(request, form.get_user())
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', { 'form' : form })
