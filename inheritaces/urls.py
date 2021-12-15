from django.urls import path
from .views import *
urlpatterns = [
    path('student/',student),
    path('place/', place),
    path('story/', story),
]
