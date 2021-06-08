from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
from todo.forms import Todo_forms
from django.contrib.auth.decorators import login_required
from .models import TODO

@login_required(login_url='login_view')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = Todo_forms()
        todos = TODO.objects.filter(user = user)
        return render(request , 'todo/index.html' , context={'form' : form , 'todos' : todos})

def signup(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        return redirect('login_view')

    context = {
        'form': form,
    }
    return render(request, "todo/signup.html", context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "todo/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url='login_view')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = Todo_forms(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else: 
            return render(request , 'todo/index.html' , context={'form' : form})

@login_required(login_url='login_view')
def delete_todo(request , id ):
    TODO.objects.get(pk = id).delete()
    return redirect('home')

@login_required(login_url='login_view')
def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')
