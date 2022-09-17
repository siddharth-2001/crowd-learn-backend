import imp
from venv import create
from django.urls import path
from .views import all_teachers, create_teacher

urlpatterns = [
    path('all', all_teachers),
    path('create', create_teacher)
]