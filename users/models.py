from django.db import models

# Create your models here.
is_staff = models.BooleanField(default=False)  # If true, this person is a Staff
user = User.objects.create_user(email='staff@example.com', password='12345')
user.is_staff = True
user.role = 'staff'
user.save()
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)
def view_for_staff_only(request):
    return HttpResponse("Staff content.")
