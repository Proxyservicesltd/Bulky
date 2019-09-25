from django import forms
from .models import BulkNumbers

class BulkSmsForm(forms.ModelForm):
    
    class Meta:
        model = 
        fields = ("name", "phone_number")