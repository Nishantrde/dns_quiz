from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('r1', r1),
    path('r1_ans', r1_ans)
]


