from django.urls import path
from .views import Information, TaskInfo


urlpatterns = [
    path('f/', Information.as_view(), name = "info"),
    path('task/', TaskInfo.as_view(), name = 'task')
]
