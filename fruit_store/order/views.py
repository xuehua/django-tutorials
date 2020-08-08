from django.shortcuts import render
from .forms import OrderForm

def get_order(request):
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            pass
    else:
        form = OrderForm()
    return render(request, "order/index.html", {'form': form})

