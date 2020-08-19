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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dojo'] = forms.ModelChoiceField(queryset=Dojo.objects.all(), 
                empty_label='-select a dojo-') 