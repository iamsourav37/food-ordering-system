from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.price}"



