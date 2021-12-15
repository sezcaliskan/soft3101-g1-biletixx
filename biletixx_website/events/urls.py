from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('events/search', views.search, name="search"),
    

    

]
