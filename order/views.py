from django.http import HttpResponse
from django.shortcuts import render
from .models import Order, Book
from book.models import Book

# Create your views here.
def orders(request):
    context = {
        'orders': Order.objects.all(),
        'books': Book.objects.all(),

    }
    return render(request, 'order/orders.html', context)