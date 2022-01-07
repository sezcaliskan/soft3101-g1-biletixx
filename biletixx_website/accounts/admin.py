from django.contrib import admin
from .models import RegisteredUser, User, Address

admin.site.register(RegisteredUser)
admin.site.register(User)
admin.site.register(Address)
