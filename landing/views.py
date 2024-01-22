from django.shortcuts import render, redirect
from administration.models import Collect, EvenementCampagne
from administration.forms import NewslettersForm, MessageForm, VolunteerForm
from administration.models import Newsletters, Volunteer, Contacts
from django.contrib import messages

# Create your views here.

def home(request):
    collects = Collect.objects.filter(confirmer = 1, posted = 1, is_amount_reached = 0).order_by('-created_at')[:3]
    campagnes = EvenementCampagne.objects.all().order_by('-created_at')[:1]
    context = {
        'collects' : collects,
        'campagnes' : campagnes
    }
    return render(request, 'landing/pages/index.html', context)

def blog(request):
    return render(request, 'landing/pages/blog.html')


def newsletter(request):
    if request.POST :
        newsletterForm = NewslettersForm(request.POST)
        if newsletterForm.is_valid():
            newsletterForm.save()
            message_success = "Votre email a bien été enregistré"
            messages.success(request, message_success)
            print("ok") 
        else :
            email = request.POST.get('email')
            check = Newsletters.objects.filter(email = email)
            if check :
                message_error = "Cet email est deja enregistré"
                messages.warning(request, message_error)
                
            else :
                message_error = "Une erreur est survenue, veuillez reessayer"
                messages.error(request, newsletterForm.errors)
                
    return redirect('index')

def message(request):
    if request.POST :
        messageForm = MessageForm(request.POST)
        if messageForm.is_valid():
            messageForm.save()
            message_success = "Votre message a bien été envoyé"
            messages.success(request, message_success)
            email = request.POST.get('email')
            check = Contacts.objects.filter(email = email)
            if not check :
                contact = Contacts(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
                contact.save()
        else :
            message_error = "Une erreur est survenue"
            print(messageForm.errors)
            messages.error(request, message_error)
            messages.warning(request, messageForm.errors)
    return redirect('index')

def volunteer(request):
    if request.POST :
        volunteerForm = VolunteerForm(request.POST, request.FILES)
        if volunteerForm.is_valid():
            volunteerForm.save()
            message_success = "Votre demande a bien été envoyé"
            messages.success(request, message_success)
        else :
            email = request.POST.get('email')
            check = Volunteer.objects.filter(email = email)
            if check :
                message_warning = "un volontaire avec cet email existe déja"
                messages.warning(request, message_warning)
            else :
                message_error = "Une erreur est survenue"
                messages.error(request, message_error)
                messages.warning(request, volunteerForm.errors)
    return redirect('index')
