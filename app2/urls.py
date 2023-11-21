from app2.views import *

from django.urls import path

app_name='muscle'

urlpatterns=[
    path('old/',old,name='old'),
]