from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms import ModelForm

from accounts.models import RegisteredUser, User, Address


class EventHolderSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_eventholder = True
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class RegisteredUserSignUpForm(UserCreationForm):
    fields = ("username", "email", "password")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","first_name", "last_name", "email")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_registereduser = True
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()
        registereduser = RegisteredUser.objects.create(user=user)
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name"]


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('addressname', 'address', 'country','city','ZIP')
        labels = {
        'addressname': 'addressname',
        'address':'address ',
        'country': 'country',
        'city': 'city',
        'ZIP': 'zip',
        

        }

        widgets = {
            'addressname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Name'}),
            'address': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Address'}),
            'country': forms.Select(attrs={'class':'form-select', 'placeholder':'Country'}),
            'city': forms.Select(attrs={'class':'form-select', 'placeholder':'City'}),
            'ZIP': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ZIP'}),
            
        }