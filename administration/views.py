from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from avatar.models import Avatar
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
import datetime as dt
# Create your views here.






#  pages 
@login_required(login_url='login')
# @permission_required()
def home(request):
    return render(request, 'administration/pages/home.html')

@login_required(login_url='login')
def admins(request):
    user = request.user
    avatars = Avatar.objects.all()
    admins = User.objects.all().order_by('-date_joined')
    
    context = {
        'admins' : admins,
        'avatars' : avatars,
    }
    return render(request, 'administration/pages/admins.html', context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def details_collect(request, collect_pk):
    collect = get_object_or_404(Collect, pk = collect_pk)
    dons = DonCollect.objects.filter(collect = collect).order_by('-date')
    context = {
        'collect' : collect,
        'dons' : dons
    }
    return render(request, 'administration/pages/collections/details.html', context)



@login_required(login_url='login')
def events(request):
    events = EvenementCampagne.objects.all().order_by('-created_at')
    organisateurs = User.objects.all()
    types_evenement = [
        'Don de sande',
        'campagne medical'
    ]
    context = {
        'events' : events,
        'organisateurs' : organisateurs,
        'type_events' : types_evenement,
        'form' : EvenementCampagneForm()
    }
    return render(request, "administration/pages/events/event_list.html", context)

@login_required(login_url='login')

def event_details(request, event_pk):
    event =  get_object_or_404(EvenementCampagne, pk = event_pk)
    context = {
        'event' : event
    }
    return render(request, "administration/pages/events/event_details.html", context)


def list_contacts(request):
    contacts = Contacts.objects.all().order_by('-date')
    context = {
        'contacts' : contacts
    }
    return render(request, 'administration/pages/contacts/list.html', context)

def list_messages(request, message_pk):
    messages = Message.objects.all().order_by('read')
    try :
        message = Message.objects.get(id = int(message_pk))
        message_edit = Message.objects.filter(id = int(message_pk))
        message_edit.update(read = 1)
    except :
        message = None
        if  message_pk != "inbox" :
            return HttpResponse(status=404)
    context = {
        "messages_all" : messages,
        "message_display" : message
    }
    return render(request, 'administration/pages/contacts/messages.html', context)

def list_newsletters(request):
    newsletters = Newsletters.objects.all().order_by('-date')
    context = {
        "newsletters" : newsletters
    }
    return render(request, 'administration/pages/contacts/newsletters.html', context)


@login_required(login_url='login')
def profile(request):
    return render(request, 'administration/pages/account/profile.html')


# end pages 




@login_required(login_url='login')
def addUser(request):
    if request.POST :
        addUserForm = AddUserForm(request.POST)
        if addUserForm.is_valid() :
            user = addUserForm.save()
            message = f"l'utilisateur {user.username} a ete crée"
            messages.success(request, message)
        else :
            message = 'une erreur est survenue veuiller reesayer'
            messages.error(request, message)
            messages.warning(request, addUserForm.errors)
    return redirect('admins')

@login_required(login_url='login')
def editUser(request, pk):
    user = User.objects.get(pk = pk)
    current_user = request.user
    if request.POST :
        try :
            avatar = Avatar.objects.get(user = current_user)
            avatarForm = AvatarForm(request.POST, request.FILES, instance=avatar)
        except :
            avatar = Avatar.objects.filter(user = current_user)
            avatar.delete()
            avatarForm = AvatarForm(request.POST, request.FILES)
        if avatarForm.is_valid():
            avatarForm.save()
        else :
            print(avatarForm.errors)
        editUserForm = EditUserForm(request.POST, instance=user)
        if editUserForm.is_valid():
            editUserForm.save()
            messages.success(request, "Vos modifications ont été enrigistrées")
        else :
            messages.warning(request, editUserForm.errors)
    else :
        editUserForm = EditUserForm(instance=current_user)
    if user == current_user :
        return redirect('profile')
    else :
        return redirect('admins')


@login_required(login_url='login')
def admins_actions(request, admin_pk , action):
    user = request.user
    admin = User.objects.get(pk = admin_pk)
    admin_to_action = User.objects.filter(pk = admin_pk)
    if action == 'delete':
        admin.delete()
        message = f"l'utilisateur {admin.username} a été supprimé"
        messages.warning(request, message)
    elif action == 'desable' :
        admin_to_action.update(is_active = False)
        message = f"l'utilisateur {admin.username} a été desactivé"
        messages.warning(request, message)
    elif action == 'activate' :
        admin_to_action.update(is_active = True)
        message = f"l'utilisateur {admin.username} a été desactivé"
        messages.info(request, message)       
    return redirect('admins')


@login_required(login_url='login')
def action_collects(request, action, collect_pk):
    collect = Collect.objects.filter(pk = collect_pk)
    if action == 'confirm' :
        collect.update(confirmer = 1)
        message = f"la collecte a ete confirméé "
        messages.success(request, message)     
    elif action == 'delete' :
        collect.delete()
        message = f"la collecte a ete retirée "
        messages.warning(request, message)
    elif action == 'post':
        collect.update(posted = 1)
        message = f"la collecte a ete publiée "
        messages.info(request, message)
    elif action == 'unpost':
        collect.update(posted = 0)
        message = f"la collecte a ete dépubliée "
        messages.info(request, message)
    return redirect('collects') 


@login_required(login_url='login')
def addCollect(request):
    if request.POST :
        addCollectForm = AddCollectForm(request.POST, request.FILES)
        if addCollectForm.is_valid() :
            addCollectForm.save()
        else :
            messages.warning(request, addCollectForm.errors)
        return redirect('collects')
    
@login_required(login_url='login')
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
                

@login_required(login_url='login')
def create_event(request):
    if request.POST :
        eventForm = EvenementCampagneForm(request.POST, request.FILES)
        if eventForm.is_valid():
            eventForm.save()
            message = "l'evenement a été crée !"
            messages.success(request, message)
        else :
            message = "l'evenement n'a pas été crée !"
            messages.warning(request, eventForm.errors)       
    return redirect('events')

@login_required(login_url='login')
def delete_newsletters(request, pk):
    email = get_object_or_404(Newsletters, pk = pk)
    email.delete()
    message = f"{email} a été supprimé "
    messages.warning(request, message)
    return redirect('newsletters')

def exportEmails(request, type):
    if type == 'JSON' :
        date = dt.datetime.today().strftime("%d-%m-%Y")
        print(date)
        file_dir = 'administration/docs/json'
        file_name = f'newslettersemail-{date}.json'
        file = f'{file_dir}/{file_name}'
        with open(file, 'w') as f :
            emails = Newsletters.objects.all().order_by('-date')
            data = []
            for email in emails :
               user = {
                   'email' : email.email,
                   'status' : email.status,
                   'date' : email.date.strftime('%d-%m-%Y')
               }
               data.append(user)
            json.dump(data, f , indent=4)
        message = f'le fichier {file_name} a été creé !'
        messages.success(request, message)
    return redirect('newsletters')

def delete_avatar(request):
    user = request.user 
    avatar = get_object_or_404(Avatar, user = user)
    avatar.delete()
    return redirect('profile')