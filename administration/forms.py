from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class AddUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("is_superuser", "is_staff", "first_name", "last_name", "email", "username")


class EditUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('__all__')

class AddCollectForm(forms.ModelForm):
    
    class Meta:
        model = Collect
        fields = ('__all__')
        
class DonCollectForm(forms.ModelForm):
    
    class Meta:
        model = DonCollect
        fields = ('__all__')

class DonneurForm(forms.ModelForm):
    
    class Meta:
        model = Donneur
        fields = ("__all__")

