from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage, name= "index"),
    # path('admin/', admin, name= 'admin'),
    path('tasks/', TaskViews.as_view(), name= "tasks"),
    path('tasks/<int:pk>', TaskDetail.as_view(), name = 'detail'),
    path('category/', CategoryView.as_view(), name='cat'),
    path('category/<int:pk>', CategoryDetail.as_view(), name = 'cat_task'),
]
