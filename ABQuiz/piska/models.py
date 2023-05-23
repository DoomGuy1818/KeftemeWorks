from django.db import models

# Create your models here.
class Teams(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=75)
    score=models.IntegerField()

class Questions(models.Model):
    id=models.IntegerField(primary_key=True)
    text=models.CharField(max_length=1000)
    answer=models.CharField(max_length=400)
    score=models.IntegerField()

class Students(models.Model):
    id=models.IntegerField(primary_key=True)
    team_id=models.ForeignKey(Teams, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    surname=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)