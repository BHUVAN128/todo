from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task
from django.urls import reverse


def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")

def mark_as_done(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect("home")

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("home")

def mark_as_undone(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = False
    task.save()
    return redirect("home")

def edit_task(request, pk):
    get_task = Task.objects.get(id=pk)
    if request.method == "POST":
         new_task = request.POST['task']
         get_task.task =new_task
         get_task.save()
         return redirect("home")
       
    else:
       context = {
          'get_task': get_task
       } 
    return render(request, 'edit_task.html',context )

