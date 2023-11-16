from django import forms
from .models import *

class ColumnCardForm(forms.ModelForm):
    
    class Meta:
        model = ColumnCard
        fields = ("title", "column", "added_by")
        
        
class WorkspaceColumnForm(forms.ModelForm):
    
    class Meta:
        model = WorkspaceColumn
        fields = ("__all__")
