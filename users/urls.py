# users/urls.py
from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    UserDetailAPIView,
    UserProfileUpdateAPIView,
    UserListAPIView
)



urlpatterns = [
    # Authentication endpoints
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    
    # User profile endpoints
    path('profile/', UserDetailAPIView.as_view(), name='user-detail'),
    path('profile/update/', UserProfileUpdateAPIView.as_view(), name='profile-update'),
    
    # Admin endpoints
    path('list/', UserListAPIView.as_view(), name='user-list'),
]
