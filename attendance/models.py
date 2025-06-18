from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Attendance(models.Model):
    CHECK_STATUS = (
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attendances"
    )
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=CHECK_STATUS, default='checked_in')
    date = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"




