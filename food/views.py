from django.shortcuts import render
from .models import Food
from order.models import Order
from customer.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.


def food_list(request):
    context = {}
    foods = Food.objects.all()
    context['foods'] = foods
    return render(request, "food_list.html", context)


@login_required(login_url='home.login')
def orders(request):
    context = {}
    user = Profile.objects.get(user=request.user)
    all_orders = Order.objects.filter(user=user)
    context['orders'] = all_orders
    return render(request, "user_orders.html", context)
