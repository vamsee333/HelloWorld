from .views import index,about
from django.urls import path

urlpatterns=[
    path('home/',index,name="index"),
    path('about/',about,name='about'),
]