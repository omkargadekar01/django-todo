from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        if title:
            Task.objects.create(title=title, due_date=due_date or None)
        return redirect('index')
    
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'todo/index.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('index')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.due_date = request.POST.get("due_date") or None
        task.save()
        return redirect('index')
    return render(request, 'todo/edit.html', {'task': task})
