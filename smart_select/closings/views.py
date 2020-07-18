from django.shortcuts import render
from .models import Firm, Employee, Organization
# Create your views here.
def firm_list(request):
    firms = Firm.objects.all()
    return render(request, 'closings/firms.html', {'firms':firms})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'closings/employees.html', {'employees':employees})

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'closings/organizations.html', {'organizations':organizations})