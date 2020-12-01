from django.shortcuts import render
from django.core.mail import send_mail

from .forms import EmailPostForm


def post_comment(request):
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['comments']
            email = cd['email']
            send_mail(subject, message, email, ['xuehua@gmail.com'])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, "contact.html", {'form': form, 'sent': sent})