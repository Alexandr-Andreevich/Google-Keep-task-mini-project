

from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib import auth


def page_for_ghost(request):
    tasks = Task.objects.all()
    return render(request, 'page_for_ghost.html', {'tasks': tasks})


def page_for_user(request):
    tasks = Task.objects.all()
    return render(request, 'page_for_user.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = Task.objects.create(title=title)
        return redirect('user_page')


def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('user_page')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST['title']
        task.title = title
        task.save()
        return redirect('user_page')
    return render(request, 'edit_task.html', {'task': task})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Такой пользователь уже существует!'})
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Пароли не совпадают!'})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user_page')
        else:
            return render(request, 'login.html', {'error': 'Введены неверные данные!'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
