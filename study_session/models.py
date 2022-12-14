from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User
from learner.models import Learner
from teacher.models import Teacher

# Create your models here.

class StudySession (models.Model):
    student   = models.ForeignKey(Learner, default= None, on_delete=models.CASCADE)
    title     = models.CharField(max_length= 64)
    details   = models.TextField()
    date_time = models.DateTimeField()
    teacher   = models.ForeignKey(Teacher, default = None, on_delete=models.CASCADE, null=True)
    meet_link = models.URLField(default="")