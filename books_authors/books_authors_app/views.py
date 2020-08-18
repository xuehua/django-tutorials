from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Book, Author
from .forms import AddAuthorForm, AddBookForm

# Create your views here.
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'desc']
    template_name = "book_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] =  Book.objects.all()
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["add_author_form"] = AddAuthorForm(context['book'])
        context["add_author_form"] = AddAuthorForm()
        return context

class AuthorCreateView(CreateView):
    model = Author
    template_name = "author_create.html"
    fields = ["first_name", "last_name", "notes"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all() 
        return context

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["add_book_form"] = AddBookForm(context['author'])
        context["add_book_form"] = AddBookForm()
        return context


def add_author(request, pk):
    book = get_object_or_404(Book, id=pk)
    author_id = request.POST['author']
    author = get_object_or_404(Author, id=author_id)
    book.authors.add(author)
    book.save()
    return redirect('book_detail', pk=pk)


def add_book(request, pk):
    author = get_object_or_404(Author, id=pk)
    book_id = request.POST['book']
    book = get_object_or_404(Book, id=book_id)
    book.authors.add(author)
    book.save()
    return redirect('author_detail', pk=pk)

    
    