from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'taskview', TasksViewSet)

urlpatterns = [
    path('tasks/', include(router.urls)),
    path('category-list/', CategoryListGenerics.as_view()),
    path('category-list/<int:pk>/', CategoryDetailsGenerics.as_view()),

]
