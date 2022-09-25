import imp
from django.urls import path
from .views import all_sessions, create_session, set_teacher, related_session


urlpatterns = [
    path('all', all_sessions),
    path('create', create_session),
    path('set', set_teacher ),
    path('related', related_session)
]