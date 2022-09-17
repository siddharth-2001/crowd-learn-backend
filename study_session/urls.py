import imp
from django.urls import path
from .views import all_sessions


urlpatterns = [
    path('all', all_sessions),
]