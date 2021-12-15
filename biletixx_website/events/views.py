from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import EventFilter
from .models import *


def home(request):
    return render(request, 'events/home.html', {})



def search(request):
    
    
    event_list = Event.objects.all()
    event_filter = EventFilter(request.GET,queryset=event_list)
   
    
    return render(request, 'events/search.html', {'filter': event_filter})




    
