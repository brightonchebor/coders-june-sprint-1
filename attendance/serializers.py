from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Attendance
        fields = ['id', 'username', 'date', 'check_in', 'check_out']
        read_only_fields = ['id', 'username', 'date', 'check_in', 'check_out']