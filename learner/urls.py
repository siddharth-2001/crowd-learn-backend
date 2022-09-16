import imp
from django.urls import path
from .views import register, all_learners, search_learner, login_user, login_token


urlpatterns = [
    path('register', register),
    path('all', all_learners),
    path('search', search_learner),
    path('login', login_user),
    path('login_token',login_token),
]