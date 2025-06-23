from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_staff_user = models.BooleanField(default=False)
    is_community_member = models.BooleanField(default=False)

    # Extra fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure only staff users get admin access
        self.is_staff = self.is_staff_user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
