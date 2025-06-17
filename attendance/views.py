from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils import timezone
from datetime import date
from .models import Attendance
from .serializers import AttendanceSerializer


class CheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today = date.today()
        attendance, created = Attendance.objects.get_or_create(user=request.user, date=today)

        if attendance.check_in:
            return Response({
                'error': 'Already checked in today',
                'check_in_time': attendance.check_in
            }, status=status.HTTP_400_BAD_REQUEST)

        attendance.check_in = timezone.now()
        attendance.save()
        serializer = AttendanceSerializer(attendance)

        return Response({
            'message': 'Checked in successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class CheckOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today = date.today()
        try:
            attendance = Attendance.objects.get(user=request.user, date=today)
        except Attendance.DoesNotExist:
            return Response({
                'error': 'No check-in record found for today'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not attendance.check_in:
            return Response({
                'error': 'Must check in first'
            }, status=status.HTTP_400_BAD_REQUEST)

        if attendance.check_out:
            return Response({
                'error': 'Already checked out today',
                'check_out_time': attendance.check_out
            }, status=status.HTTP_400_BAD_REQUEST)

        attendance.check_out = timezone.now()
        attendance.save()
        serializer = AttendanceSerializer(attendance)

        return Response({
            'message': 'Checked out successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class TodayStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        try:
            attendance = Attendance.objects.get(user=request.user, date=today)
            serializer = AttendanceSerializer(attendance)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Attendance.DoesNotExist:
            return Response({'message': 'No attendance record for today'}, status=status.HTTP_200_OK)


class AttendanceHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attendances = Attendance.objects.filter(user=request.user).order_by('-date')
        serializer = AttendanceSerializer(attendances, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
