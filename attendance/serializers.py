from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'id',
            'date',
            'check_in_time',
            'check_out_time',
            'status',
        ]
        read_only_fields = fields
