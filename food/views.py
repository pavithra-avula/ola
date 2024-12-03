from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def veg(request):
    return HttpResponse('<h1>Life of Pure Vegetarians is waste</h1>')

def nonveg(request):
    return render(request,'nonveg.html')