from django.urls import path, include
from . import views
urlpatterns = [
    path('firms/', views.firm_list, name='firms_list' ),
    path('employees/', views.employee_list, name='employees_list'),
    path('organizations/', views.organization_list, name='organization_list')
]
