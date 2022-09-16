from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Learner(models.Model):

    user          = models.OneToOneField(User, on_delete= models.CASCADE)
    qualification = models.CharField(max_length=64)
    rating        = models.IntegerField(default=0)
    lec_given     = models.IntegerField(default=0)
    lec_taken     = models.IntegerField(default=0)