from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def student(req):
    s = Student.objects.get(first_name= 'Mona')
    s2= Student.objects.filter(age =10)
    print(s)
    print(s2)
    return HttpResponse("Abstract Inheritance")

def place (req):
    p = Place.objects.filter(place_name = 'Little Women')
    c = Cafe.objects.filter(place_name = 'Little Women')
    print(p)
    print(c)
    return HttpResponse("Mult_table inheritance")


def story(req):
    story = Story.objects.filter(type='f')
    fiction = FictionStory.objects.all()
    print(story)
    print(fiction)
    return HttpResponse("Proxy inheritance")





