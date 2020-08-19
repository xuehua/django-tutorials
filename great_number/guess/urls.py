from django.urls import path
from .views import guess

urlpatterns = [
    path('', guess, name='guess'),
]