from django.contrib import admin
from .models import ContactList, DeletedUser
# Register your models here.


admin.site.register(ContactList)
admin.site.register(DeletedUser)


