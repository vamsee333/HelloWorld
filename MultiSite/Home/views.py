from django.shortcuts import render
from .models import HomePageItems
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("helllo world ")

def about(request):
    return HttpResponse('this a new hybrid website')


