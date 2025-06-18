# users/urls.py
from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserDetailAPIView

urlpatterns = [
    path("api/register/", RegisterAPIView.as_view(), name="user-register"),
    path("api/login/",    LoginAPIView.as_view(),    name="user-login"),
    path("api/me/",       UserDetailAPIView.as_view(), name="user-detail"),
]
