
from django import forms
from .models import Category, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description', 'priority', 'date_added','category']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'date_added': forms.SelectDateWidget(),        
        }
       

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'descriotion']
        labes = {
            'category_name': 'Category Name',
            'descriotion' :'Description'
        }

