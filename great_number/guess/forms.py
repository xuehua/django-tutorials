from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class GuessForm(forms.Form):
    guess = forms.IntegerField(
                validators = [
                    MaxValueValidator(100), 
                    MinValueValidator(1),
                ]
            )


