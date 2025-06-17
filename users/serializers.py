from rest_framework import serializers
from . models import CommuityMembers, Staff

class CommunityMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMembers
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    model = Staff
    fields = '__all__'