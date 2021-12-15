from django.db import models


# Create your models here.
"""
    Abstract Inheritance:
"""
class Info(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    class Meta:
        abstract = True
        ordering = ['age']

class Student(Info):
    GRADE = [ 
        ('Elementry','Elementry'),
        ('Middle','Middle'),  
        ('High','High'),
    ]
    grade = models.CharField(choices=GRADE, max_length=10)

    def __str__(self) -> str:
        return self.first_name

class Teacher(Info):
    COURSES =[ 
        ('English','English'),
        ('Math','Math'),
        ('Physics','Physics'),
        ('Science','Science'),
    ]
    courses = models.CharField(choices=COURSES, max_length=10)
    def __str__(self) -> str:
        return self.last_name



"""
    Multi_table Inhetitance:
"""

class Place(models.Model):
    place_name = models.CharField(max_length=100)
    address = models.TextField()
    def __str__(self) -> str:
        return self.place_name

class Cafe(Place):
    active = models.BooleanField(default=False)
    food = models.CharField(max_length=100)

class Supplier(Place):
    customers = models.ManyToManyField(Place , related_name='provider')


"""
    proxy inheritance:
"""

class Story(models.Model):
    STORY_TYPES = (
    ('f', 'Fiction'),
    ('n', 'Non_fiction'),
    ('b', 'Bigraphy'),
)
    type = models.CharField(max_length=1, choices=STORY_TYPES)
    title = models.CharField(max_length=100)
    body = models.TextField()
    def __str__(self) -> str:
        return self.title

class FictionManager(models.Manager):
    def get_queryset(self) :
        return super().get_queryset().filter(type = 'f')


class FictionStory(Story):
    objects = FictionManager()
    class Meta:
        ordering = ['title']
        proxy= True


