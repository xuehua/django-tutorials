from django import forms

class EmailPostForm(forms.Form):
    first_name = forms.CharField(max_length=25,
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=25,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
    subject = forms.CharField(max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Subject'}))

    comments = forms.CharField(widget=forms.Textarea)
    