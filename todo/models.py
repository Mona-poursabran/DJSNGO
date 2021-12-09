from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    descriotion = models.TextField()
    
    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Task (models.Model):
    PRIORITY=[
        ("high","high"),
        ("medium", "medium"),
        ("low","low")
    ]
    category =models.ManyToManyField(Category,related_name='category_tasks', related_query_name='cat_tasks')
    title = models.CharField(max_length=40)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY)
    date_added = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title

