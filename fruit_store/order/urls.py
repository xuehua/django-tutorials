from django.urls import path
from . import views

urlpatterns = [
    #path('', views.get_order, name="get_order"),
    #path('checkout/', views.checkout, name="checkout")
    path('', views.get_order1, name="get_order"),
    path('checkout/', views.checkout1, name="checkout"),
]