from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from avatar.models import Avatar
from .forms import *
from .models import *
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

@login_required
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

@login_required
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

@login_required
def collects(request):
    user = request.user
    collects = Collect.objects.all().order_by('-created_at')
    my_collects = Collect.objects.filter(by = user.pk)
    collect_en_attentes = Collect.objects.filter(confirmer = 0).order_by('-created_at')
    collect_en_cours = Collect.objects.filter(confirmer = 1, is_amount_reached = 0).order_by('-created_at')
    collect_bouclees = Collect.objects.filter(is_amount_reached = 1).order_by('-created_at')
    addCollectForm = AddCollectForm()
    
    donCollectForm = DonCollectForm()
    
    context = {
        'my_collects' : my_collects,
        'collects' : collects,
        'addCollectForm' : addCollectForm,
        'collect_en_attentes' : collect_en_attentes,
        'collect_en_cours' : collect_en_cours,
        'collect_bouclees' : collect_bouclees,
        'donCollectForm' : donCollectForm
    }
    return render (request, 'administration/pages/collections.html', context)

@login_required
def details_collect(request, collect_pk):
    collect = get_object_or_404(Collect, pk = collect_pk)
    dons = DonCollect.objects.filter(collect = collect).order_by('-date')
    print(dons)
    context = {
        'collect' : collect,
        'dons' : dons
    }
    return render(request, 'administration/pages/collections/details.html', context)

@login_required
def action_collects(request, action, collect_pk):
    collect = Collect.objects.filter(pk = collect_pk)
    if action == 'confirm' :
        collect.update(confirmer = 1)
        print('confirmed')
    elif action == 'delete' :
        collect.delete()
    elif action == 'post':
        collect.update(posted = 1)
    elif action == 'unpost':
        collect.update(posted = 0)
    return redirect('collects') 

@login_required
def addCollect(request):
    if request.POST :
        addCollectForm = AddCollectForm(request.POST, request.FILES)
        if addCollectForm.is_valid() :
            addCollectForm.save()
        else :
            print('unvalidated')
        return redirect('collects')
    

def donCollect(request):
    if request.POST:
        donCollectForm = DonCollectForm(request.POST)
        if donCollectForm.is_valid():
            donCollectForm.save()
            collect_pk = request.POST['collect']
            collect = Collect.objects.filter(pk = collect_pk)
            collect_raised = Collect.objects.get(pk = collect_pk)
            amount = request.POST['amount']
            collect.update(raised = collect_raised.raised + int(amount))
            print(collect_raised.raised )
            print(collect_raised.goal)
            if int(collect_raised.raised) >= int(collect_raised.goal) :
                collect.update(is_amount_reached = 1)
            
            donneur_email = request.POST['donneur_email']
            try :
                donneur = Donneur.objects.get(email = donneur_email)
            except Donneur.DoesNotExist :
                donneur_name = request.POST['donneur_name']
                total_don = request.POST['amount']
                donneur = Donneur(name = donneur_name, email = donneur_email, total_don = total_don)
                donneur.save()
    return redirect('collects')
                

