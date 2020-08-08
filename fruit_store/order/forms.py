from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class OrderForm(forms.Form):
    strawberry = forms.TypedChoiceField(label="Strawberry", choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    raspberry = forms.TypedChoiceField(label="Raspberry", choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    apple = forms.TypedChoiceField(label="Apple", choices=PRODUCT_QUANTITY_CHOICES, coerce=int)

    student_name = forms.CharField(label="Name:", max_length=50)
    student_id = forms.CharField(label="Your Student ID:", max_length=50)