from django.shortcuts import render
from django.shortcuts import redirect

from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import EventFilter
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import ListView, FormView
from events.models import Ticket, Booking
from django.http import HttpResponse




def home(request):
    return render(request, 'events/home.html', {})



def list_events(request):
    
    
    event_list = Event.objects.all()
    event_filter = EventFilter(request.GET,queryset=event_list)
    event_list = event_filter.qs
    
    context = { 'event_filter':event_filter ,'event_list':event_list }
    return render(request, 'events/list_events.html', context)


def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    
    context = { 'event':event }
    return render(request, 'events/show_event.html', context)

    

def add_event(request):
    submitted = False

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = request.user # logged in user
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})
    


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, ("Event Deleted!!"))
        return redirect('list_eventholder_events')      
    else:
        messages.success(request, ("You Aren't Authorized To Delete This Event!"))
        return redirect('list_eventholder_events')  
  
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list_eventholder_events')

    context = { 'event':event , 'form':form }
    return render(request, 'events/update_event.html', context)


def list_eventholder_events(request):
    me = request.user.id
    event_list = Event.objects.filter(manager=me)
    context = { 'event_list':event_list }
    return render(request, 'events/list_eventholder_events.html', context)




def my_tickets_view(request):

    bookings = Booking.objects.filter(user=request.user) 
    
    context = { 'bookings':bookings }
    return render(request,'events/my_tickets.html', context)


class TicketList(ListView):
    model = Ticket
    


class BookingList(ListView):
    model = Booking


def BookingView(request):
    #booking_instance = Booking.objects.create(ticket_id=1,user=request.user)
    #return HttpResponse(booking_instance)
    context = {  }
    return render(request, 'events/booking_view.html', context)





   
                 




    
       




