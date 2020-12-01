from django import forms

class EmailPostForm(forms.Form):
    first_name = forms.CharField(max_length=25, label="First Name:",
        widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=25, label="Last Name:",
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(label="Email:",
        widget=forms.EmailInput(attrs={'class':"form-control",'placeholder': 'Enter Email'}))
    subject = forms.CharField(max_length=100, label="Subject:", 
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Enter Subject'}))
    comments = forms.CharField(label="Comments:",
        widget=forms.Textarea(attrs={'class':"form-control", "rows":5}))
    