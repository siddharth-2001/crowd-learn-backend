import imp
from django.urls import path
from .views import all_sessions, create_session, set_teacher


urlpatterns = [
    path('all', all_sessions),
    path('create', create_session),
    path('set', set_teacher )
]