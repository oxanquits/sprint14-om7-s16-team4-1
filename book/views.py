from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Book, Author

# Create your views here.


def books(request):
    context = {
        'books': Book.objects.all(),
        'title': 'Книги',

    }
    return render(request, 'book/books.html', context)


def books_sorted_by_names(request):
    context = {
        'books': Book.objects.all().order_by('name'),
        'title': 'Книги, сортування за назвою А - Я'
    }
    return render(request, 'book/books.html', context)


def books_sorted_by_names_desc(request):
    context = {
        'books': Book.objects.all().order_by('-name'),
        'title': 'Книги, сортування за назвою Я - А'
    }
    return render(request, 'book/books.html', context)


def books_sorted_by_count(request):
    context = {
        'books': Book.objects.all().order_by('count'),
        'title': 'Книги, сортування за кількістю'
    }
    return render(request, 'book/books.html', context)


def book_by(request, bookid):

    context = {
        'book': Book.get_by_id(bookid),
        'authors': get_authors(Book.get_by_id(bookid).authors.all()),
    }
    return render(request, 'book/book.html', context)


def get_authors(authorslist):
    authors = [
        f'{author.surname} {author.name} {author.patronymic}' for author in authorslist]
    return ', '.join(authors)


def add_book(request):
    if request.method == 'POST':
        form = AddBookPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddBookPostForm()
    return render(request, 'book/add_book.html', {'form': form})
