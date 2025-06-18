from django.urls import path
from .views import *

urlpatterns = [
    path('api/check_in', CheckInView.as_view(), name='check_in'),
    path('api/check_in', CheckInView.as_view(), name='check_in'),
]
