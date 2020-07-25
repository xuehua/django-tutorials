from django.urls import path
from . import views

urlpatterns = [
    path('blog-search/', 
        views.BlogPage.as_view(template_name='blog_search.html'), 
        name='blog-search'),
    path('search/', 
        views.BlogAutoCompletePage.as_view(),
        name = 'blog-autocomplete'),
    path('search/autocomplete/', 
        views.autocomplete, 
        name ='autocomplete'),
]

