from django.shortcuts import render, redirect
import datetime
from .forms import OrderForm

def get_order(request):
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            request.session['order'] = form.cleaned_data
            order = request.session['order']
            order['total'] = int(order['strawberry']) + int(order['raspberry']) + int(order['apple'])
            order['created'] = datetime.datetime.now().strftime("%B %d, %Y")
            #request.session.modified = True
            return redirect("checkout")
    else:
        form = OrderForm()
    return render(request, "order/index.html", {'form': form})


def checkout(request):
    order = request.session['order']
    return render(request, "order/checkout.html", {'order':order})

def get_order1(request):
    form = OrderForm()
    return render(request, "order/index1.html", {'form': form})

def checkout1(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data
            order['total'] = int(order['strawberry']) + int(order['raspberry']) + int(order['apple'])
            order['created'] = datetime.datetime.now().strftime("%B %d, %Y")
            #return render(request, "order/checkout.html", {'order': order} )   
    else: 
    #form = OrderForm()
        order = {}
        order['strawberry']=0
        order['raspberry']=0
        order['apple'] = 0
        order['total'] =0
        order['student_name'] = ''
        order['student_name'] = ''
        order['created'] = datetime.datetime.now().strftime("%B %d, %Y")
    return render(request, "order/checkout.html", {'order': order} )
    #return redirect("get_order") 
        