# Community models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Attendance(models.Model):
    user = models.models.OneToOneField(User, on_delete=models.CASCADE)
    date= models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=(
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ), default='present')
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"