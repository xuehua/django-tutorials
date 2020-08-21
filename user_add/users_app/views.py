from django.shortcuts import render, redirect, get_list_or_404
from .models import User
from .forms import UserForm
def user_list_view(request):
    user_list = get_list_or_404(User)
    user_form = UserForm()
    return render(request, "user_list.html", 
                {'user_list':user_list, 
                'user_form': user_form})