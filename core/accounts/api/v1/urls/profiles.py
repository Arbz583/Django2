from django.urls import path, include
from ..views import *



urlpatterns = [

    path('', ProfileApiView.as_view(), name='profile'),

]