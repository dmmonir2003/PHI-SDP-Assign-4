from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):

    if request.method=='POST':
        category_form=forms.TaskForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_task')
    else:
        category_form=forms.TaskForm()
    return render(request,'add_task.html',{'forms': category_form})


def edit_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task_form=forms.TaskForm(instance=task)
    if request.method=='POST':
        task_form=forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
   
    return render(request,'add_task.html',{'forms': task_form})



def delete_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')