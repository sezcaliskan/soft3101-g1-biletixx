# from django.urls import include, path
# from . import views

# urlpatterns = [
 #    path('login_user', views.login_user, name="login"),

# ]

from django.urls import include, path

from . import views

urlpatterns = [
    
    #path('login_user', views.login_user, name="login"),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('registration/', views.RegisteredUserSignUpView.as_view(), name='registereduser_signup'),
    path('accounts/signup/eventholder/', views.EventHolderSignUpView.as_view(), name='eventholder_signup'),
    path('profile/', views.profile, name='profile'),
]