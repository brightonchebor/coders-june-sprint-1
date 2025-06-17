from django.urls import path
from .views import CheckInView, CheckOutView

urlpatterns = [
    path('API/checkin/', CheckInView.as_view(), name='check-in'),
    path('API/checkout/', CheckOutView.as_view(), name='check-out'),
]
