from django.urls import path

from .views import index, contact, register, login, logout, user_account, change_username, change_password, delete_account


urlpatterns = [
    path("", index, name="home.home"),
    path("contact-us/", contact, name="home.contact"),
    path("register/", register, name="home.register"),
    path("login/", login, name="home.login"),
    path("logout/", logout, name="home.logout"),
    path("user-account/", user_account, name="home.account"),
    path("user-account/change-username", change_username, name="home.change_username"),
    path("user-account/change-password", change_password, name="home.change_password"),
    path("user-account/delete-account", delete_account, name="home.delete_account"),
]
