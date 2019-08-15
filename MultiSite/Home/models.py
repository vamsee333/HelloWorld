from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HomePageItems(models.Model):
    Topics=models.CharField(max_length=50)
    PlaceItems=models.CharField(max_length=100)
    Explore=models.CharField(max_length=100)


class FAQ(models.Model):
    question_text=models.CharField(max_length=200)
    added_date=models.DateTimeField('publised date')

class RelatedAnswers(models.Model):
    question=models.ForeignKey(FAQ,on_delete=models.CASCADE)
    ChoiceText=models.CharField(max_length=50)
    votes=models.IntegerField(default=0)

