# Community models.py
from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
   ROLE_CHOICES = [
       ('attache', 'Attache'),
       ('member', 'Member'),
       ('visitor', 'Visitor'),
       ('not_sure', 'Not Sure'),
   ]
   
   DEPARTMENT_CHOICES = [
       ('communication', 'Communication'),
       ('creatives', 'Creatives'),
       ('tech', 'Tech'),
       ('community_experience', 'Community Experience'),
       ('youth_engagement', 'Youth Engagement'),
       ('heritage', 'Heritage'),
       ('finance', 'Finance'),
       ('entrepreneurship', 'Entrepreneurship'),
   ]
   
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone_number = models.CharField(max_length=17)
   role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
   department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
   
   def __str__(self):
       return f"{self.user.get_full_name()} - {self.get_role_display()}"
   
   class Meta:
       verbose_name_plural = "Community Members"