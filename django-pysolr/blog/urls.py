from django.urls import path
from . import views

urlpatterns = [
    path('', 
        views.BlogListView.as_view(), 
        name='blog_list'),
    path('create/', 
        views.BlogCreateView.as_view(),
        name = 'blog_create'),
    path('<int:pk>/',
        views.BlogDetailView.as_view(),
        name='blog_detail'),
    path('search/', 
        views.SearchView.as_view(), 
        name= 'blog_search'),
    path('search_autocomplete/', 
        views.SearchAutocompleteView.as_view(),
        name = 'search-autocomplete'),
    path('search_autocomplete/title/', 
        views.autocomplete_title, 
        name = 'autocomplete_title'),
    path('search_autocomplete/detail/',
        views.autocomplete_detail,
        name = 'autocomplete_detail')
]

