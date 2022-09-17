from rest_framework import serializers
from .models import StudySession

class StudySerializer(serializers.ModelSerializer):

    class META:
        model = StudySession
        fields = '__all__'
