from distutils.log import error
from unittest import result
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Learner
from .serializers import LearnerSerializer
from django.contrib.auth import login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@api_view(['POST'])
def register(request):

    data = request.data

    request = request._request
    json_response  = {}

    try:
        user = User.objects.create_user(email = data["email"],username = data["email"],password = data["password"], first_name = data["first_name"], last_name = data["last_name"])
        user.save()
        login(request, user)
        learner = Learner.objects.create(user=user, qualification = data["qualification"])
        learner.save()
        #create token for new registered user
        token = RefreshToken.for_user(user)
        
        json_response['access'] = str(token.access_token)
        json_response['refresh'] = str(token)

        return Response(json_response, status=201)
    except:
    
        json_response['message'] = 'Error'
        return Response(json_response, status=401)
    

@api_view(['POST'])
def login_token(request):

    try :

        json_response = {}

        auth = JWTAuthentication()
        data = auth.authenticate(request)
        user = data[0]

        login(request,user)
        json_response["message"] = "Logged In"
        return Response(json_response, status=200)

    except :

        json_response["message"] = "Couldn't Login"
        return Response(json_response,status=400)
    

@api_view(['POST'])
def login_user(request):

    response_json = {}

    try:
   
        data = request.data

        request = request._request
    
        user = authenticate(request, username = data["email"], password = data["password"])

        token = RefreshToken.for_user(user)

        login(request,user)
        
        response_json["access"] = str(token.access_token)
        response_json["refresh"] = str(token)
        response_json["message"] = "Logged In"

        return Response(response_json, status=200)

    except :
        response_json["message"] = "Incorrect Data"
        return Response(response_json, status= 401)
    
    
@api_view(['GET'])
def all_learners(request):
    learners = Learner.objects.all()
    serializer = LearnerSerializer(learners, many = True)
    return Response(data = serializer.data, status=200)

@api_view(['POST'])
def search_learner(request):
    data = request.data
    learner = Learner.objects.get(id = data["id"])
    result  = User.objects.get(learner = learner)
    json_response = {"email" : result.email}
    return Response(json_response, status=200)
