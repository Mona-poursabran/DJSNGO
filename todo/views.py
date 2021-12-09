
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from todo.forms import CategoryForm, TaskForm
from .models import Category, Task
from datetime import datetime
from django.db.models import Max, Count
from django.core import serializers


def homepage(req):

#     if req.method == 'POST'  and req.is_ajax():
#             text = req.POST.get('task')
            
#             p = Task.objects.filter(title__startswith=text)
#             if p:
#                 return JsonResponse({
#                     'tasks':list(p.values_list('title', flat=True))
#                 })
#             else:
#                 return JsonResponse({
#                     'tasks': [],
#                     'msg' : "doesn't match any files",
#                 })
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

# def home(req):
#     form = TaskForm()
#     return render(req, 'todo/index.html',{'form': form})


# def todo_list(req):
#     todos = Task.objects.all()
#     return JsonResponse({'todos': list(todos.values())})



### Quesion20 / save info in database as json and get form
class TasksView(View):
    form_class = TaskForm
    template_name = 'todo/taskview.html'

    def get(self, *args, **kwargs):
        form = self.form_class
        tasks = Task.objects.all()
        return render(self.request, self.template_name, {'form': form, 'tasks': tasks})

    def post(self, *args, **kwargs ):
        if self.request.is_ajax and self.request.method == 'POST':
            form = self.form_class(self.request.POST)
            if form.is_valid():
                new_task = form.save()
                ser_new_task= serializers.serialize('json', [new_task])
                # send to client side
                return JsonResponse({'new_task': ser_new_task}, status= 200)
            else:
                return JsonResponse({"error": form.errors}, status = 400)
        return JsonResponse({"error": ""}, status= 400)


class TaskViews(ListView):
    model = Task
    template_name = 'todo/tasks.html'

    queryset = Task.objects.order_by('date_added') #todo


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    





  
### Question20 Three buttons to show some tasks
def home_task(req):
    return render(req, 'todo/info_tasks.html')

def task_all(req):
    task_all= Task.objects.all()
    return JsonResponse({'task_all': list(task_all.values())})
## Question20
def expired_list(req):
    expired_taks = Task.objects.all()
    return JsonResponse({'expired_taks': list(expired_taks.filter(date_added__lt =datetime.now()).values_list('title', flat=True))})  
## Question20
def unexpired_list(req):
    unexpired_task= Task.objects.all()
    return JsonResponse({'unexpired_task': list(unexpired_task.filter(date_added__gt =datetime.now()).values_list('title', flat=True))})  
## Question20
def last_list(req):
    last_task = Task.objects.all()
    return JsonResponse({'last_task':list(last_task.order_by('-id')[0:3].values_list('title', flat=True))})



class CategoryView(ListView):
    model = Category
    template_name = 'todo/category.html'

    
class CategoryDetail(DetailView):
    model = Category
    template_name = 'todo/catdetail.html'

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context ['task'] = Task.objects.all()
        return context



### Question20 let see some tasks in each category
def categorydetail(req, id):
    category = Category.objects.get(id = id)
    title = category.category_tasks.all()
    print('category', category)
    print('title', title)
    context={
        'category':category,
        'title' : title
    }
    return render (req, 'todo/catdetail.html', context)



### Question20/ Create a new category
class NewCategory(View):
    form_class = CategoryForm
    template_name = 'todo/new_cat.html'

    def get(self, *args, **kwargs):
        form = self.form_class
        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs ):
        if self.request.is_ajax and self.request.method == 'POST':
            form = self.form_class(self.request.POST)
            if form.is_valid():
                new_category = form.save()
                ser_new_category= serializers.serialize('json', [new_category])
                # send to client side
                return JsonResponse({'new_category': ser_new_category}, status= 200)
            else:
                return JsonResponse({"error": form.errors}, status = 400)
        return JsonResponse({"error": ""}, status= 400)
    


def new_category(req):
    if req.method != 'POST':
        form = CategoryForm()
    else :
        form = CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(req, 'todo/new_cat.html', context)


### Question20 Two buttons to show some categories
def empty_category(req):
    empty_cat = Category.objects.filter(cat_tasks__title__isnull= True)
    return JsonResponse({'empty_cat':list(empty_cat.values_list('category_name', flat=True))})

def popular_category(req): # :(
    total_num = Category.objects.annotate(count =Count('cat_tasks__title'))
    for i in range(len(total_num)):
        print(total_num[i], total_num[i].count)
    return JsonResponse({'empty_cat':''})
 
