from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Contact
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
    
    