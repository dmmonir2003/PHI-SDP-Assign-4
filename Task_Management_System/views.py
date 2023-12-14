from django.shortcuts import render
from task.models import TaskModel
# Create your views here.


def home(request):
    task=TaskModel.objects.all()
    return render(request,('home.html'),{'data':task})