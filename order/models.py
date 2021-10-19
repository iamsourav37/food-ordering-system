from django.db import models
from customer.models import Profile
from food.models import Food
import uuid
# Create your models here.


class Order(models.Model):
    STATUS_TYPE = (
        ("Preparing", "Preparing your order"),
        ("Dispatched", "Your order is dispatched"),
        ("Delivered", "Order is delivered successfully"),
    )

    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    food_details = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_TYPE, default=STATUS_TYPE[0][0])

    def __str__(self):
        return f"{self.created_at}, {self.status}"
