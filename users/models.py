from django.db import models
from django.utils import timezone


class CommunityMembers(models.Model):

    ROLE_CHOICES = (
        ('member', 'Member'),
        ('visitor', 'Visitor'),
        ('attachee', 'Attachee'),
        ('not_sure', 'Not Sure'),
    )

    DEPARTMENT_CHOICES = (
>>>>>>> 71982b236429a7e22470a85521c2274a8bc7bcd3
        ('communication', 'Communication'),
        ('creatives', 'Creatives'),
        ('tech', 'Tech Department'),
        ('community_experience', 'Community Experience'),
        ('youth_engagement', 'Youth Engagement'),
        ('heritage', 'Heritage'),
        ('admin', 'Admin'),
        ('finance', 'Finance'),
        ('entrepreneurship', 'Entrepreneurship'),
<<<<<<< HEAD
    ]
 #fill your details here
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField() 
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    sign_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def check_out(self):
        self.check_out_time = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} ({self.reason})"
=======
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)

   
   
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['role', 'department']

    def __str__(self):
        return self.phone_number

<<<<<<< HEAD
=======
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
        unique_together = ('user', 'date')  # Prevent double sign-ins
# Create your models here.


class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50)

 def __str__(self):
 return f"{self.name} ({self.who are you})"

    
>>>>>>> 71982b236429a7e22470a85521c2274a8bc7bcd3
