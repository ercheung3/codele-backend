from django.db import models

   #EXTENSION
    #HELP model ex. Youtube Links, Resource Links
    #TYPE model ex. Array, String Manipulation, etc...
# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    source = models.CharField(max_length=32,blank=True)
    link = models.CharField(max_length=128,blank=True)
    difficulty = models.IntegerField(default=0)
 
