from django.shortcuts import render, HttpResponse, redirect
from .models import Food
from order.models import Order
from customer.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
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


@require_POST
@login_required(login_url='home.login')
def order_food(request, id):
    context = {}
    try:
        user = Profile.objects.get(user=request.user)
        specific_food = Food.objects.get(id=id)
        order = Order(user=user, food_details=specific_food)
        order.save()
        return redirect(orders)
    except:
        return HttpResponse("invalid id")
