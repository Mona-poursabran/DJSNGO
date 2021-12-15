from django.urls import path
from .views import statusview
urlpatterns = [
    path('status/', statusview)
]
