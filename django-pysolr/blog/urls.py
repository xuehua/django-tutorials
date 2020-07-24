from django.urls import path
from . import views

urlpatterns = [
    path('blog-search/', 
        views.BlogPage.as_view(template_name='blog_search.html'), 
        name='blog-search'),
    path('blog-autocomplete/', 
        views.BlogAutoCompletePage.as_view(template_name='blog_autocomplete.html'), 
        name ='blog-autocomplete'),
]

