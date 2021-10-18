from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20)
    place = models.CharField(max_length=200)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}"