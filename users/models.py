from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class Users(models.Model):
    ROLE_CHOICES = (
        ('member', 'Member'),
        ('visitor', 'Visitor'),
        ('attachee', 'Attachee'),
        ('not_sure', 'Not sure'),
    )

    DEPARTMENT_CHOICES = (
        ('communication', 'Communication'),
        ('creatives', 'Creatives'),
        ('tech', 'Tech Department'),
        ('community_experience', 'Community Experience'),
        ('youth_engagement', 'Youth Engagement'),
        ('heritage', 'Heritage'),
        ('admin', 'Admin'),
        ('finance', 'Finance'),
        ('entrepreneurship', 'Entrepreneurship'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.role}"

    class Meta:
        unique_together = ('user', 'date')  

class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.wh})"

    

