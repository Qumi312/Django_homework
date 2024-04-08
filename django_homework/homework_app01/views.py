from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello World</h1><p>This start pager</p>')


def about(request):
    return HttpResponse('<h1>About</h1>')
