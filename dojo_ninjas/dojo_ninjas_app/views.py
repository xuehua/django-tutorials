from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Dojo
from .forms import DojoForm, NinjaForm

class DojoListView(ListView):
    model = Dojo
    context_object_name = "dojo_list"
    template_name = "dojo_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_dojo_form"] = DojoForm()
        context['add_ninja_form'] = NinjaForm()
        return context
    
def add_dojo(request):
    if request.method == 'POST':
        form = DojoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("home")

def add_ninja(request):
    if request.method == 'POST':
        form = NinjaForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("home")

def delete_dojo(request, pk):
    dojo = get_object_or_404(Dojo, id=pk)
    dojo.delete()
    return redirect("home")


