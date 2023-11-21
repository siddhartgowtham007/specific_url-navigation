from app1.views import *

from django.urls import path

app_name='mustang1967'

urlpatterns=[
    path('new/',new,name='new'),
]