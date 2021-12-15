from django.contrib import admin
from .models import Student, Teacher, Place, Cafe, Supplier, Story, FictionStory
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Cafe)
admin.site.register(Supplier)
admin.site.register(Story)
admin.site.register(FictionStory)