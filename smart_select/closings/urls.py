from django.urls import path, include
from . import views
urlpatterns = [
    path('firms/', views.firms_list, name='firms_list' ),
    path('employees/', views.employees_list, name='employees_list'),
]
