from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from accounts.forms import  EventHolderSignUpForm, RegisteredUserSignUpForm, UserUpdateForm
from accounts.models import  RegisteredUser,  User
from accounts.forms import UserCreationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import logout
from .forms import *
from django.http import HttpResponseRedirect



def user_list(request):

    list = User.objects.all()

    return render(request, "registration/user_list.html",{'list':list})

def user_delete(request, pk):
    u = User.objects.filter(email=pk)
    u.delete()

    return redirect('user_list')

def profile(request):
    current_user = request.user
    context = {
       'user': current_user
    }
    return render(request, 'registration/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form':user_form
    }
    return render(request, 'registration/profile_update.html', context)




class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class RegisteredUserSignUpView(CreateView):
    model = User
    form_class = RegisteredUserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'registereduser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class EventHolderSignUpView(CreateView):
    model = User
    form_class = EventHolderSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'eventholder'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')



def add_address(request):
    submitted = False

    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.addressowner = request.user # logged in user
            form.save()
            return HttpResponseRedirect('/add_address?submitted=True')
    else:
        form = AddressForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'registration/add_address.html', {'form':form, 'submitted':submitted})
    


def delete_address(request, address_id):
    address = Address.objects.get(pk=address_id)
    if 2>1:
        address.delete()
        messages.success(request, ("Address Deleted!!"))
        return redirect('address_list')      
    else:
        messages.success(request, ("You Aren't Authorized To Delete This Address!"))
        return redirect('address_list')  
  
def update_address(request, address_id):
    address = Address.objects.get(pk=address_id)
    form = AddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('address_list')

    context = { 'address':address , 'form':form }
    return render(request, 'registration/update_address.html', context)


def address_list(request):
    me = request.user.id
    address_list = Address.objects.filter(addressowner=me)
    context = { 'address_list':address_list }
    return render(request, 'registration/address_list.html', context)






   

   


