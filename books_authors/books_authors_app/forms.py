from django import forms 
from .models import Book, Author

class AddAuthorForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                    empty_label='-select an author-')

    # def __init__(self, book=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     ids = book.authors.values_list('id', flat=True)
    #     self.fields['author'] = forms.ModelChoiceField(queryset=Author.objects.exclude(id__in=ids), 
    #             empty_label='-select an author-') 


class AddBookForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(),
                    empty_label='-select a book-')

    # def __init__(self, author=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     ids =author.books.values_list('id', flat=True)
    #     self.fields['book'] = forms.ModelChoiceField(queryset=Book.objects.exclude(id__in=ids), 
    #             empty_label='-select a book-')                 