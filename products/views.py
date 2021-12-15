from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def statusview(req):
    p1= Product.objects.all()
    s_p1= Product.status_result.available()
    s_p2 = Product.status_result.unavailable()
    print('all:', p1)
    print('avialable: ', s_p1)
    print('unavialable: ', s_p2)
    return HttpResponse('Welcome')
