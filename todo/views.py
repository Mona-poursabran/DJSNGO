from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Category, Task
from datetime import datetime
from django.contrib import messages

# Create your views here.
# def admin(req):
#     return render(req, 'todo/admin.html')

def homepage(req):
    task = Task.objects.all().order_by('-id')[0:3]
    category = Category.objects.all()
    

    if req.method == 'POST':
        c = req.POST.get('cat')
        t = req.POST.get('title')
        p = req.POST.get('priority')
        d = req.POST.get('description')
        time = req.POST.get('time')
       
        tasks = Task(Category= Category.objects.get(category_name = c) , title = t, priority= p, description= d, date_added= time )
        tasks.save() 
    context = {
        'category' :category,
        'tasks': task, 
        }
    
    return render(req, 'todo/index.html', context)


class TaskViews(ListView):
    model = Task
    template_name = 'todo/tasks.html'

    queryset = Task.objects.order_by('date_added') #todo

class TaskDetail(DeleteView):
    model = Task
    template_name = 'todo/task_detail.html'



class CategoryView(ListView):
    model = Category
    template_name = 'todo/category.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'todo/test.html'

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context ['task'] = Task.objects.all()
        return context








# def category_task(req):
#     tasks = Task.objects.all()
#     categories = Category.objects.all()
#     context ={
#         'task': tasks,
#         'category' : categories
#     }
#     return render(req, 'todo/category.html', context )