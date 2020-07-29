import json
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import render, get_object_or_404
from django.views.generic import (TemplateView, ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from haystack.query import SearchQuerySet
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Blog

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

class BlogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Blog
    template_name = "blog/home.html"
    permission_required = 'blog.view_blog'
    permission_denied_message = "You don't have permission to view blogs"

class MyBlogListView(BlogListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class AllBlogListView(BlogListView):
    permission_required = ('blog.view_blog', 'blog.view_all_blogs')
    permission_denied_message = "You don't have permission to view blog or view all blogs" 


class FollowingBlogListView(BlogListView):

    def has_permission(self):
        if not super().has_permission():
            return False

        self.permission_denied_message = f"Access denied, you are not following '{self.kwargs['username']}'."
        following = self.request.user.following.all().values_list('username', flat=True)
        return self.kwargs['username'] in following

    def get_queryset(self):
        sqs = super().get_queryset()
        user = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        return sqs.filter(author=user)



class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Blog    
    template_name = "blog/detail.html"
    permission_required = 'blog.view_blog'

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'summary', 'description']
    template_name = "blog/create.html"
    permission_required = 'blog.add_blog'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'summary', 'description']
    template_name = "blog/update.html"
    permission_required = 'blogg.change_blog'

class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/delete.html"
    success_url = reverse_lazy("blog_list")
    permission_required = 'blog.delete_blog'