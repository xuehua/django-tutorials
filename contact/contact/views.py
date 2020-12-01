from django.shortcuts import render
from .forms import EmailPostForm
# Create your views here.
def post_comment(request):
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
    else:
        form = EmailPostForm()
    return render(request, "contact.html", {'form': form})