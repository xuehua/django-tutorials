from django.shortcuts import render
from .models import Firm, Employee
# Create your views here.
def firms_list(request):
    firms = Firm.objects.all()
    return render(request, 'closings/firms.html', {'firms':firms})

def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'closings/employees.html', {'employees':employees})