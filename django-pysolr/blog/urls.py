from django.urls import path
from . import views

urlpatterns = [
    path('blog-search/', 
        views.BlogPage.as_view(template_name='blog_search.html'), 
        name='blog-search'),
    path('search/title', 
        views.BlogAutoCompletePage.as_view(),
        name = 'blog-search-title'),
    path('search/autocomplete_title/', 
        views.autocomplete_title, 
        name ='autocomplete_title'),
    path('search/detail/',
        views.BlogSearchDetailPage.as_view(),
        name = 'blog-search-detail'),
]

