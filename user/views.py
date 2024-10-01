from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError, DatabaseError

# Create your views here.
#renders login view and login user to the system
def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

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

#logout the user from the system
def logoutView(request):
    if request.method == "POST":
        try:
            logout(request)
            return redirect('home')
        except IntegrityError:
            return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
        except DatabaseError:
            return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })