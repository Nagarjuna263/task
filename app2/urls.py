from django.urls import path
from app2.views import *
app_name='nag'

urlpatterns = [
    path('queen/',queen,name='queen'),
    path('marry/',marry,name='marry'),
]
