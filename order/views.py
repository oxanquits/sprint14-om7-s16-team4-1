from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Order, Book
from book.models import Book
from .forms import *

# Create your views here.


def orders(request):
    context = {
        'orders': Order.objects.all(),
        'books': Book.objects.all(),

    }
    return render(request, 'order/orders.html', context)


def add_order(request):
    if request.method == 'POST':
        form = AddOrderPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = AddOrderPostForm()
    return render(request, 'order/add_order.html', {'form': form})
