from django.core.exceptions import PermissionDenied
from rest_framework import generics, viewsets,permissions, status
from rest_framework.response import Response
from .models import Task, Category
from .permissions import *
from .serializer import *


"""
    Every user is able to see their tasks and task detail
    Task List and Task Detail 
    this class is able to create, update and delete a task :)
""" 
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        owner = self.request.user
        is_staff= self.request.user.is_superuser
        if is_staff:
            return Task.objects.all()
        return Task.objects.filter(owner = owner)


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
   
 

"""
    Every user is able to see their categories
    this class shows a list of categories and user can create a new one
"""
class CategoryListGenerics (generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated ]

    def get_queryset(self):
        owner = self.request.user
        is_superuser= self.request.user.is_superuser
        if is_superuser:
            return Category.objects.all() 
        return Category.objects.filter(owner = owner)
   
   
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



"""
    Every user is able to see their category detail and just update it
    this class is written to show each category with update ability :)
"""
class CategoryDetailsGenerics (generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated,
                            ISOwner]


    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        else :
            return Response(status.HTTP_204_NO_CONTENT)
  

 
