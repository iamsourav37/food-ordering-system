from django.db import models

# Create your models here.


class ContactList(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} : {self.phone_no}"


class DeletedUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=22)
    place = models.CharField(max_length=200)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

