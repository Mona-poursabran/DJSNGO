from django import forms
from datetime import datetime
from .models import Task
from django.core.exceptions import ValidationError
class InfForm(forms.Form):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField(required=True)
    Date = forms.DateField(help_text="What's today's date?", widget=forms.SelectDateWidget())



    def clean_age(self):
        super(InfForm, self).clean()
        age = self.cleaned_data.get('age')
        if int(age) < 18:
            self.__errors['age'] = self.error_class(["You are not allowed to submit!"])
        return age
    
 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_date']

        widgets= {
            "title": forms.TextInput(attrs={"placeholder":"enter a title"}),
            "description": forms.Textarea(attrs={"col":50, "row":3}),
            "category": forms.CheckboxSelectMultiple(),
            "date_added": forms.SelectDateWidget()
        }