from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todo_app/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        ToDo.objects.create(title=title)
    return redirect('index')

def edit(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)

    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.save()
        return redirect('index')
    
    return render(request, 'todo_app/edit.html', {'todo': todo})

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


# Create your views here.
