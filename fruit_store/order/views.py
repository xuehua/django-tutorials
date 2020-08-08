from django.shortcuts import render

def get_order(request):
    return render(request, "template/index.html")
