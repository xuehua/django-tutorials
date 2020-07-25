from django.urls import path
from . import views

urlpatterns = [
    path('blog-search/', 
        views.BlogPage.as_view(template_name='blog_search.html'), 
        name='blog-search'),
    path('search/title/', 
        views.BlogSearchTitlePage.as_view(),
        name = 'blog-search-title'),
    path('search/title/autocomplete/', 
        views.autocomplete_title, 
        name ='autocomplete_title'),
    path('search/detail/',
        views.BlogSearchDetailPage.as_view(),
        name = 'blog-search-detail'),
    path('search/detail/autocomplete/',
        views.autocomplete_detail,
        name = 'autocomplete_detail')
]

