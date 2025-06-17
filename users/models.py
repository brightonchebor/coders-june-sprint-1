from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CommunityMembers(models.Model):

    ROLE_CHOICES = (
        ('member', 'Member'),
        ('visitor', 'Visitor'),
        ('attachee', 'Attachee'),
        ('not_sure', 'Not Sure'),
    )

    DEPARTMENT_CHOICES = (
        ('communication', 'Communication'),
        ('creatives', 'Creatives'),
        ('tech', 'Tech Department'),
        ('admin', 'Admin'),
        ('finance', 'Finance'),ent'),
        ('community_experience', 'Community Experience'),
        ('youth_engagement', 'Youth Engagement'),
        ('heritage', 'Heritage'),
        ('entrepreneurship', 'Entrepreneurship'))
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField() 
    reason = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    sign_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def check_out(self):
        self.check_out_time = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} ({self.reason})"

    
class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.wh})"

    

