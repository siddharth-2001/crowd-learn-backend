from datetime import datetime
from ftplib import all_errors
from rest_framework.response import Response
from rest_framework.decorators import api_view

from teacher.models import Teacher
from .serializers import StudySerializer
from .models import StudySession
from django.contrib.auth.models import User
from learner.models import Learner

from learner.serializers import UserSerializer


# Create your views here.

@api_view(['GET'])
def all_sessions(request):

    all_sessions = StudySession.objects.all()
    serializer   = StudySerializer(all_sessions, many = True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_session(request):

    json_response = {}

    try:
       
        data = request.data

        user = User.objects.get(email = data['email'])

        student = Learner.objects.get(user = user)

        new_session = StudySession.objects.create(student = student, date_time = datetime.now(),title = data['title'],details = data['details'])

        new_session.save()

        serializer = StudySerializer(new_session)

        json_response = serializer.data

        learner_id = json_response["student"]
        related_user = User.objects.get(learner_id = learner_id)
        user_serializer = UserSerializer(related_user)
        json_response["student"] = user_serializer.data

        json_response['message'] = 'Success'

        return Response(serializer.data, status= 200)

    except:
        json_response['message'] = 'Failed to create Study Session'

        return Response(json_response, status= 400)

@api_view(['POST'])
def set_teacher(request):

    data    = request.data
    user    = User.objects.get(email = data['email'])
    teacher = Teacher.objects.get_or_create(user = user)[0]
    session = StudySession.objects.get(id = data['id'])
    session.teacher = teacher
    session.save()

    serializer = StudySerializer(session)

    return Response(serializer.data, status = 200)



