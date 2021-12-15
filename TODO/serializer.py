from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import Task, Category



class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    category = SlugRelatedField(queryset=Category.objects,many= True, slug_field='category_name')
    class Meta:
        model = Task
        fields = ['id','title', 'priority', 'date_added', 'category', 'owner']
        # fields= '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    category_tasks = serializers.StringRelatedField(many= True, read_only = True)
    class Meta:
        model = Category
        fields = ['id','category_name', 'owner', 'category_tasks']



