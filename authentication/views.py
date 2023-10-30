from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def login_admin(request):
    if request.POST :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None and (user.is_superuser or user.is_staff) and user.is_active :
                login(request, user)
                return redirect('home')
            else :
                print('nope')
    else :
        form = AuthenticationForm(request)
    
    return render(request, 'authentication/pages/login.html')

def logout_admin(request):
    logout(request)
    return redirect('login')