from django.contrib import admin
from .models import RegisteredUser, User

admin.site.register(RegisteredUser)
admin.site.register(User)
