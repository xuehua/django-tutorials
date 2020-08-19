from django.urls import path
from . import views

urlpatterns = [
    path('', views.DojoListView.as_view(), name='home'),
    path('add_dojo/', views.add_dojo, name='add_dojo'),
    path('add_ninja/', views.add_ninja, name='add_ninja'),
    path('delete_dojo/<pk>/', views.delete_dojo, name='delete_dojo'),
]