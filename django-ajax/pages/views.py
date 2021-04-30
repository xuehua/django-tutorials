from django.shortcuts import render
from common.decorators import ajax_required
# Create your views here.
def homepage(request):
    return render(request, 'index.html')

@ajax_required
def ajax(request):
    info = {'top_track': 'Equilibrium', 'top_artist': 'Celine Dion'}
    return render(request, 'ajax.html', {'info':info})