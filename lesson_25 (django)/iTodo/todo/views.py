from django.shortcuts import render
from .models import Todo


def home(request):
    return render(request, 'todo/home.html')


def about(request, pk=None):
    if pk:
        todos = Todo.objects.filter(id=pk)
    else:
        todos = Todo.objects.all()

    return render(request, 'todo/about.html', {'todos': todos})
