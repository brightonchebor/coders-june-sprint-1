from django.db import models
from django.utils import timezone

#create your models 
class CommunityMember(models.Model):
 # Reason choices
 WHO ARE YOU_CHOICES = [
 ('attachee', 'Attachee'),
 ('staff', 'Staff'),
 ('visitor', 'Visitor'),
 ('member', 'Member'),
 ('not_sure', 'Not Sure'),
 ]

 # Department choices
 DEPARTMENT_CHOICES = [
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
 first name = models.CharField(max_length=100)
 last name = models.CharField(max_length=100)
 phone_number = models.CharField(max_length=15)
 email = models.EmailField() 
 who are you = models.CharField(max_length=20, choices=WHO ARE YOU_CHOICES)
 department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
 sign_in_time = models.DateTimeField(default=timezone.now)
 check_out_time = models.DateTimeField(null=True, blank=True)

 def check_out(self):
 self.check_out_time = timezone.now()
 self.save()

 def __str__(self):
 return f"{self.name} ({self.who are you})"


