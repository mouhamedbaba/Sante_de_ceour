from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
@csrf_exempt
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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try :
                email = User.objects.get(email = username)
                user = authenticate(username = email.username, password = password)
                if user is not None and (user.is_superuser or user.is_staff) and user.is_active :
                    login(request, user)
                    return redirect('home')
            except :
                messages.error(request, 'identifiant incorrect')
            return redirect('login')
    else :
        form = AuthenticationForm()
    
    return render(request, 'authentication/pages/login.html')


def logout_admin(request):
    logout(request)
    return redirect('login')