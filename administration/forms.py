from django import forms
from django.contrib.auth.models import  User
from .models import *
class AddUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username",'first_name','last_name', 'email', 'is_staff', 'is_superuser', 'password')
        

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

