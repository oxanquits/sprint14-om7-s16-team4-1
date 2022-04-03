from django.http import HttpResponse
from django.shortcuts import render
from .models import Author
from book.models import Book

# Create your views here.
def authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'author/authors.html', context)

def author_books(request, authorid):
    print(authorid)
    context = {
        'books': Book.objects.filter(authors = authorid),
        'author': Author.get_by_id(authorid)
    }
    return render(request, 'author/auth_books.html', context)
