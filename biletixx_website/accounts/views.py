from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from accounts.forms import  EventHolderSignUpForm, RegisteredUserSignUpForm
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

def profile(request):
    context = {}
    return render(request, 'registration/profile.html')



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









   

   


