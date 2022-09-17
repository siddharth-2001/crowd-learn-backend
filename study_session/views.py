from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudySerializer
from .models import StudySession
from django.contrib.auth.models import User


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

        student = User.objects.filter(email = data['email'])

        new_session = StudySession.objects.create(student = student, date_time = datetime.now(),title = data['title'],details = data['details'])

        new_session.save()

        serializer = StudySerializer(new_session)

        json_response = serializer.data

        json_response['message'] = 'Success'

        return Response(serializer.data, status= 200)

    except:

        json_response['message'] = 'Failed to create Study Session'

        Response(json_response, status= 400)