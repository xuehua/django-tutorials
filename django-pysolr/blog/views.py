from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog
from haystack.query import SearchQuerySet
import ast

# Create your views here.


class BlogPage(TemplateView):
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
