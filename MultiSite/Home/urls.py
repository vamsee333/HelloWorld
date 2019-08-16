from .views import index,about,Explore
from django.urls import path

urlpatterns=[
    path('home/<int:id>',index,name="index"),
    path('about/',about,name='about'),
    path('explore/',Explore,name='explore'),
]