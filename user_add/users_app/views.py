from django.shortcuts import render, redirect, get_list_or_404
from .models import User
from .forms import UserForm

def user_list_view(request):
    user_list = get_list_or_404(User)
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("user_list")

    return render(request, "user_list.html", 
                {'user_list':user_list, 
                'user_form': user_form})