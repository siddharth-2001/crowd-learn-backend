from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    lectures      = models.IntegerField(default= 0)
    rating        = models.FloatField(default=0.0)
    qualification = models.TextField()
