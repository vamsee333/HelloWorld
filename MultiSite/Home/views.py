from django.shortcuts import render
from .models import HomePageItems,FAQ,RelatedAnswers
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

def index(request,id):
    return HttpResponse("helllo world %s " %id)

def about(request):
    items = HomePageItems.objects.all()
    context={'items':items}
    return render(request,'homepage.html',context)

def Explore(request):
    return render(request,'explore.html',{})


def showdetail(request):
    items=FAQ.objects.all()
    date=[]
    for x in items:
        date.append(timezone.now().hour - x.added_date.hour)
    context={'items':items,'hours':date}
    return render(request,'showdetail.html',context)

