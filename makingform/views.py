from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import InfForm, TaskForm
from .models import Task
# Create your views here.

class Information(View):
    def get(self,request, *args, **kwargs):
        form = InfForm()
        return render(request,"makingform/infoform.html", {"form": form} )

"""
    This part can be written with def ;)
"""
class TaskInfo(View):
    def get(self,request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'makingform/taskform.html', {"form": form})

    def post(self,request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        return render(request, 'makingform/taskform.html', {"form":form})


        