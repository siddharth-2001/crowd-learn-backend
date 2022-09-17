from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Learner(models.Model):

    user          = models.OneToOneField(User, on_delete= models.CASCADE)
    qualification = models.TextField()
    rating        = models.FloatField(default=0)
    lectures      = models.IntegerField(default=0)