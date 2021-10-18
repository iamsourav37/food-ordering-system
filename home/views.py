from django.shortcuts import render, HttpResponse, redirect
from .models import ContactList, DeletedUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from customer.models import Profile
from django.contrib.auth import hashers
# Create your views here.


def index(request):
    return render(request, 'index.html')


def food_list(request):
    return render(request, "food_list.html")


def contact(request):
    if request.method == 'POST':
        print("post request handle here.....")
        fullname = request.POST['fullname']
        email = request.POST['email']
        place = request.POST['place']
        phone = request.POST['phone']
        contact_obj = ContactList(full_name=fullname, email=email, place=place, phone_no=phone)
        contact_obj.save()
    return render(request, 'contact_us.html')


def register(request):
    if request.user.is_authenticated:
        return redirect(index)

    context = {}
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # both the password are matched
            try:
                user = User.objects.get(username=request.POST['username'])
                context['message'] = f"{request.POST['username']} already exists. Try another !!!"
            except User.DoesNotExist:
                full_name = request.POST['name']
                first_name = full_name.split(" ")[0]
                last_name = full_name.split(" ")[-1]
                email = request.POST['email']
                pin = request.POST['pin']
                place = request.POST['place']
                phone = request.POST['phone']
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                profile = Profile(user=user, phone_no=phone, pin=pin, place=place)
                profile.save()
                auth.login(request, user)
                return redirect(index)

        else:
            context['message'] = "Password must be same"
    return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect(index)
    context = {}
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            username = user.username
            password = request.POST['password']
            auth_user = auth.authenticate(username=username, password=password)

            if auth_user is not None:
                auth.login(request, auth_user)
                return redirect(index)
            else:
                context['message'] = "Invalid Credentials !!!, Password is not matched (security hole)"

        except User.DoesNotExist:
            context['message'] = "Invalid Credentials !!!"

    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(login)


@login_required(login_url='home.login')
def user_account(request):
    context = {}
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[-1]
        pin = request.POST['pin']
        place = request.POST['place']
        phone = request.POST['phone']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        profile.pin = pin
        profile.place = place
        profile.phone_no = phone
        profile.save()
        context['success_message'] = f"Data updated successfully !!!"

    context['user'] = user
    context['profile'] = profile
    return render(request, "user_account.html", context)


@login_required(login_url='home.login')
def change_username(request):
    context = {}
    user = request.user
    context['user'] = user
    if request.method == 'POST':
        newusername = request.POST['newusername'].strip()
        if not 4 <= len(newusername) <= 15:
            context['err_message'] = f"Username must be 4 character, or maximum 15 character"
            return render(request, 'change_username.html', context)
        try:
            exists_user = User.objects.get(username=newusername)
            context['err_message'] = f"{newusername} is already exists, try another !!!"

        except User.DoesNotExist:
            user.username = newusername
            user.save()
            context['success_message'] = "Username updated successfully !!!"

    return render(request, 'change_username.html', context)


@login_required(login_url='home.login')
def change_password(request):
    context = {}
    user = request.user
    context['user'] = user
    if request.method == 'POST':
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']

        if hashers.check_password(oldpassword, user.password):
            user.set_password(newpassword)
            user.save()
            auth.login(request, user)
            context['success_message'] = "Password updated successfully"
        else:
            context['err_message'] = "Old password not matched"

    return render(request, 'change_password.html', context)


@login_required(login_url='home.login')
def delete_account(request):
    context = {}
    user = request.user
    if request.method == 'POST':
        password = request.POST['password']

        if hashers.check_password(password, user.password):
            profile = Profile.objects.get(user=user)
            deleted_user = DeletedUser(first_name=user.first_name, last_name=user.last_name, email=user.email, username=user.username, phone_no=profile.phone_no, pin=profile.pin, place=profile.place)
            deleted_user.save()
            user.delete()
            context['success_message'] = "User deleted successfully"
            return redirect(index)
        else:
            context['err_message'] = "Password not matched"

    return render(request, 'delete_account.html', context)
