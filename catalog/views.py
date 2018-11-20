from urllib import request

from django.shortcuts import get_object_or_404, render
from django.views import generic

from catalog.models import *

# function Based Views

# view for the homepage site
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)


def book_list_view(request):
    book_list = Book.objects.all()
    context = {
        'my_book_list': book_list,
    }
    return render(request, 'book_list.html', context=context)

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    context = {
        'book':book
    }
    return render(request,'catalog/book_detail.html', context=context)

# class based views

class BookDetailView(generic.DetailView):
    model = Book


# class BookListView(generic.ListView):
    
#     model = Book
#     context_object_name = 'my_book_list'
#     queryset = Book.objects.all()
#     template_name = 'books/my_arbitrary_template_name_list.html'

