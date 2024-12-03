from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def auto(request):
    return HttpResponse('<h1>Auto is a 3 wheeler vehicle</h1>')
