from django.shortcuts import render
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
    

