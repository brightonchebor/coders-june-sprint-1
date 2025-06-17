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
