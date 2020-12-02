from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from.models import Todo


def Index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def Update(request, id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'task': task, 'form': form}
    return render(request, 'Update.html', context)
    #task_object = Todo.objects.get(id=id)
    #if request.method == 'POST':
        #task = request.POST.get('Task')
        #task_object.task = task
        #task_object.save()
        #return redirect('index')
    #return render(request, 'Update.html', {'task': task_object})

def goHome(request):
    return redirect('index')

def Delete(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'Delete.html', {'task': task})

def add(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return redirect('index')

def Complete(request, id):
    task = Todo.objects.get(id=id)
    task.complete = True
    task.save()
    return redirect('index')
