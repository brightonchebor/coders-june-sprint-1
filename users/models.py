from django.db import models

class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, blank=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.username