# from django.urls import include, path
# from . import views

# urlpatterns = [
 #    path('login_user', views.login_user, name="login"),

# ]

from django.urls import include, path

from . import views

urlpatterns = [
    

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('registration/', views.RegisteredUserSignUpView.as_view(), name='registereduser_signup'),
    path('accounts/signup/eventholder/', views.EventHolderSignUpView.as_view(), name='eventholder_signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('list/', views.user_list, name='user_list'),
    path('delete/(?P<pk>\d+)/$', views.user_delete, name='user_delete'),
    path('add_address', views.add_address, name="add_address"),
    path('delete_address/<address_id>', views.delete_address, name="delete_address"),
    path('address_list', views.address_list, name="address_list"),
    path('update_address/<address_id>', views.update_address, name='update_address'),
    
  
    
]