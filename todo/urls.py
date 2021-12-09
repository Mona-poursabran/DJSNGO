from django.urls import path
from .views import *

urlpatterns = [
    path("", TasksView.as_view(), name = "index"), ##index page include form
    path('tasks/', TaskViews.as_view(), name= "tasks"), ## show list of tasks
    path('tasks/<int:pk>', TaskDetail.as_view(), name = 'detail'),  ## show details of each task
    path('category/', CategoryView.as_view(), name='cat'), ## show list of categories
    path('empty-categories/', empty_category, name ='empty-cat'), ## button which shows empty category
    path('popular-category/', popular_category, name='popular_cat'),##button which shows popular category
    # path('new_cat/', new_category, name = "new_cat"),
    path('new_cat/', NewCategory.as_view(), name = "new_cat1"), ## form category to add new one
    # path('category/<int:pk>', CategoryDetail.as_view(), name = 'cat_task'),
    path('category/<int:id>', categorydetail, name = 'cat_task'), ## details of each category
    path('tasksinfo/', home_task, name="info_tasks"), ## Task info with three buttons
    path('task-all/', task_all, name='task-all'),## show all tasks by using type get
    path('expired-list/', expired_list, name="expired-list"), ## list of expired tasks
    path('unexpired-list/', unexpired_list, name="unexpired-list"), ## list of unexpired tasks
    path('last-list/', last_list, name="last-list"), # list of three last tasks
]
