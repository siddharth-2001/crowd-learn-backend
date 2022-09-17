import email
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Teacher
from .serializer import TeacherSerializer
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET'])
def all_teachers(request):

    json_response = {}


    try:
        all_teachers = Teacher.objects.all()
        serializer = TeacherSerializer(all_teachers, many = True)

        json_response = serializer.data

        json_response['message'] = 'Success'

        Response(json_response, status=200)

    except:

        json_response['message'] = 'Failed to get all Teachers'

        Response(json_response, status = 400)


@api_view(['POST'])
def create_teacher(request):

    json_response = {}

    try:

        data = request.data
        user = User.objects.filter(email = data['email'])

        new_teacher = Teacher.objects.create(user = user)
        new_teacher.save()

        serializer = TeacherSerializer(new_teacher)
        json_response = serializer.data

        json_response['message'] = 'Success'

        return Response(json_response, status=201)

    except:

        json_response['message'] = 'Failed'
        return Response(json_response, status = 400)




