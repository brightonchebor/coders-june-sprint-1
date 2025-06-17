from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CommunityMembers, Staff
from .serializers import CommunityMemberSerializer, StaffSerializer
from django.utils import timezone



class CommunityMemberViewSet(viewsets.ModelViewSet):
    queryset = CommunityMembers.objects.all()
    serializer_class = CommunityMemberSerializer

    @action(detail=False, methods=['post'])
    def check_out(self, request, pk=None):
        member = self.get_object()
        member.check_out_time = timezone.now()
        member.save()
        return Response({"message": "checked out successfully"}, status=status.HTTP_200_OK)

class StaffViewSet(viewsets.ModelViewSet):
    querryset = Staff.objects.all()
    serializer_class = StaffSerializer
