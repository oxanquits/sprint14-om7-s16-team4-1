from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import *


def users(request):
    context = {
        'users': CustomUser.objects.all(),
    }
    return render(request, 'users.html', context=context)


def add_user(request):
    if request.method == 'POST':
        form = AddUserPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = AddUserPostForm()
    return render(request, 'add_user.html', {'form': form})


def delete_user(request, userid):
    print('DELETE')
    user = CustomUser.objects.get(pk=userid)
    user.delete()
    return redirect('users')
