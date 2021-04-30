from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def ajax(request):
    info = {'top_track': 'Equilibrium', 'top_artist': 'Celine Dion'}
    return render(request, 'ajax.html', {'info':info})