from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityMemberViewSet, StaffViewSet


router = DefaultRouter()
router.register(r'community-members', CommunityMemberViewSet, basename='community-member')
router.register(r'staff', StaffViewSet, basename='staff')

urlpatterns = [
    path('', include(router.urls)),
]