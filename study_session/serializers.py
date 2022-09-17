from rest_framework import serializers
from .models import StudySession

class StudySerializer(serializers.ModelSerializer):

    class Meta:
        model = StudySession
        fields = '__all__'
