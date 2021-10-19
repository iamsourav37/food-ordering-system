from django.urls import path
from .views import food_list, orders


urlpatterns = [
    path("", food_list, name="food.food_list"),
    path("orders/", orders, name="food.orders"),
]
