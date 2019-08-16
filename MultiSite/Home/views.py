from django.shortcuts import render
from .models import HomePageItems
# Create your views here.
from django.http import HttpResponse

def index(request,id):
    return HttpResponse("helllo world %s " %id)

def about(request):
    items = HomePageItems.objects.all()
    context={'items':items}
    return render(request,'homepage.html',context)

def Explore(request):
    return render(request,'explore.html',{})




