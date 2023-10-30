from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from avatar.models import Avatar
from .forms import *
from .models import Collect
# Create your views here.

@login_required(login_url='login')
# @permission_required()
def home(request):
    return render(request, 'administration/pages/home.html')

login_required()
def admins(request):
    user = request.user
    message = ''
    admins = User.objects.all()
    addUserForm = AddUserForm()
    context = {
        'admins' : admins,
        'addUserForm' : addUserForm,
        'message' : message,
    }
    return render(request, 'administration/pages/admins.html', context)

def addUser(request):
    if request.POST :
        addUserForm = AddUserForm(request.POST)
        if addUserForm.is_valid():
            message = f'l\'utilisateur {request.POST['username']} a ete cree'
            addUserForm.save()
        else :
            message = 'une erreur est survenue veuiller reesayer'
            print('unvalitaded')
    return redirect('admins')

def editUser(request, admin):
    if request.POST :
        editUserForm = EditUserForm(request.POST, instance=admin)
        if editUserForm.is_valid():
            editUserForm.save()
            print('edited')
        else :
            print('unvalidated')
            
    else :
        editUserForm = EditUserForm(instance=admin)
@login_required

def admins_actions(request, admin_pk , action):
    user = request.user
    admin = User.objects.get(pk = admin_pk)
    admin_to_action = User.objects.filter(pk = admin_pk)
    if action == 'delete':
        admin.delete()
    elif action == 'desable' :
        admin_to_action.update(is_active = False)
    elif action == 'activate' :
        print('admin activated')
        admin_to_action.update(is_active = True)
        print('admin activated')
        
    return redirect('admins')

login_required
def collections(request):
    user = request.user
    collects = Collect.objects.all().order_by('-created_at')
    my_collects = Collect.objects.filter(by = user.pk)
    collect_en_attentes = Collect.objects.filter(confirmer = 0)
    collect_en_cours = Collect.objects.filter(confirmer = 1, is_amount_reached = 0)
    collect_bouclees = Collect.objects.filter(is_amount_reached = 1)
    addCollectForm = AddCollectForm()
    context = {
        'my_collects' : my_collects,
        'collects' : collects,
        'addCollectForm' : addCollectForm,
        'collect_en_attentes' : collect_en_attentes,
        'collect_en_cours' : collect_en_cours,
        'collect_bouclees' : collect_bouclees
    }
    return render (request, 'administration/pages/collections.html', context)

login_required
def action_collects(request, action, collect_pk):
    collect = Collect.objects.filter(pk = collect_pk)
    if action == 'confirm' :
        collect.update(confirmer = 1)
        print('confirmed')
    elif action == 'delete' :
        collect.delete()
    return redirect('collects') 

def addCollect(request):
    if request.POST :
        addCollectForm = AddCollectForm(request.POST, request.FILES)
        if addCollectForm.is_valid() :
            addCollectForm.save()
        else :
            print('unvalidated')
        return redirect('collects')
    

