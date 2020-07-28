from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from django.views.generic.edit import CreateView
from .models import Blog
from haystack.query import SearchQuerySet
import json
from django.http import HttpResponse

# Create your views here.


class SearchView(TemplateView):
    template_name = "blog/search.html"
    def get(self, request, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, **kwargs):
        query = request.POST.get('query', '')

        results = SearchQuerySet().models(Blog).filter(content=query).load_all()
        
        # if True:
        #     # use default core schema of solr 8.5 
        #     results = [result for result in search_results]            
        # else:
        #     # use django-haystack generated schema with modifications.
        #     search_details = [result.title for result in results]
        return render(request, self.template_name, {'results': results})

class SearchAutocompleteView(TemplateView):
    template_name = 'blog/search_autocomplete.html'
    def get(self, request, **kwargs):
        return render(request, self.template_name, {})

def autocomplete_title(request):
    sqs = SearchQuerySet().autocomplete(title_auto=request.GET.get('q', '')).load_all()
    suggestions = [result.object.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')


def autocomplete_detail(request):
    sqs = SearchQuerySet().autocomplete(title_auto=request.GET.get('q', '')).load_all()
    details = []
    for result in sqs:
        blog = result.object
        details.append({
                'label':blog.title, 
                'value':blog.id, 
                'desc': blog.description})
    
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results':details
    })
    return HttpResponse(the_data, content_type='application/json')

class BlogListView(ListView):
    model = Blog
    template_name = "blog/home.html"

class BlogDetailView(DetailView):
    model = Blog    
    template_name = "blog/detail.html"

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'short_description', 'description']
    template_name = "blog/create.html"
