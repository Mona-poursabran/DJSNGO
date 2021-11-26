from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Task (models.Model):
    Category =models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField()

    priority = models.IntegerField(blank=True)
    date_added = models.DateTimeField()
   

    def __str__(self):
        return self.title

