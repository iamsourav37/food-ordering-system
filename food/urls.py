from django.urls import path
from .views import food_list, orders, order_food


urlpatterns = [
    path("", food_list, name="food.food_list"),
    path("orders/", orders, name="food.orders"),
    path("order/<str:id>", order_food, name="food.order_food"),
]
