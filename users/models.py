from django.db import models

# Create your models here.


class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    