from django.shortcuts import render
from .forms import GuessForm
import random

def guess(request):
    form = GuessForm()
    result = None
    number = request.session.get('number')
    times = request.session.get('times')

    if not number:
        request.session['number'] = random.randint(1, 100)
        number = request.session.get('number')
    
    if not times:
        request.session['times'] = 0
        times = request.session.get('times')
        
    if request.method == "POST":
        if 'play_again' in request.POST:
            request.session['number'] = random.randint(1, 100)
            request.session['times'] = 0
            number = request.session.get('number')
            times = request.session.get('times')
        else:
            form = GuessForm(request.POST)
            if form.is_valid():
                result = number - int(form.cleaned_data['guess'])
                request.session['times'] += 1
                times = request.session.get('times')
            
    return render(request, 'guess.html', 
                    {'form': form, 
                    'result': result,
                    'number': number,
                    'times': times})

