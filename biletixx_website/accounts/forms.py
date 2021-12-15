from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import RegisteredUser, User


class EventHolderSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_eventholder = True
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class RegisteredUserSignUpForm(UserCreationForm):
    fields = ("username", "email", "password")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_registereduser = True
        user.email = self.cleaned_data["email"]
        user.save()
        registereduser = RegisteredUser.objects.create(user=user)
        return user



     