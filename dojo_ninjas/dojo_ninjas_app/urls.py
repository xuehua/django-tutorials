from django.urls import path
from . import views

urlpatterns = [
    path('', views.DojoListView.as_view(), name='home'),
]