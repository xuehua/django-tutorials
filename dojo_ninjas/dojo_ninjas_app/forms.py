from django import forms
from .models import Dojo, Ninja

class DojoForm(forms.ModelForm):
    
    class Meta:
        model = Dojo
        fields = ("name", "city", "state")


class NinjaForm(forms.ModelForm):
    
    class Meta:
        model = Ninja
        fields = ("first_name", "last_name", "dojo")