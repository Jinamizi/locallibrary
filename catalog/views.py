from django.shortcuts import render
from django.db.models import Count
from django.views import generic

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books (status = 'a')
    num_instances_available= BookInstance.objects.filter(status__exact='a').count()

    #The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def get_books(request):
    books = Book.objects.annotate(instance_count=Count('bookinstance'))
    #books = Book.objects.all()
    return render(request, 'books.html', context={"books":books})

class BookListView(generic.ListView):
    model = Book

def test(request):
    books = Book.objects.annotate(instance_count=Count('bookinstance'))
    #books = Book.objects.all()
    return render(request, 'test.html', context={"books":books})

