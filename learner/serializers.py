from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Learner

class LearnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Learner
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_joined', 'last_login']