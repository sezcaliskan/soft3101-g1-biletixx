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
from events.models import Ticket
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



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

    print("my_tickets_view---user{}".format(request.user))
    tickets = Ticket.objects.filter(user=request.user) 
    
    context = { 'tickets':tickets }
    return render(request,'events/my_tickets.html', context)


class TicketList(ListView):
    model = Ticket
    


def buy_ticket(request):

    print("buy_ticket---user{}".format(request.user))

    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login') 

    event_id = request.POST.get('event_id') # isimleri html'deki gibi duzelt
    count = request.POST.get('count') 

    event = get_object_or_404(Event, pk=int(event_id))

    if event is None: 
        return redirect('home')

    ticket_list = []
    
    #satılmış biletlerin sayısı
    numOfSoldTickets = Ticket.objects.filter(event=event).count()
    #etkinliğin maksimum kapasitesi
    maksKapasite = event.max_sellable_tickets
    #etkinliğin müsait bilet sayısı
    availableCapacity = maksKapasite-numOfSoldTickets
    
    #uygun bilet sayısından fazla bilet almak isterse
    if int(count)>availableCapacity:
        return redirect('home')

    else:

         #birden fazla bilet almak isterse
        if int(count) > 1:

            for i in range (0, int('count')):
                try: 
                    ticket = Ticket(event=event, user=request.user)
                    ticket.save()
                except:
                    print("ticket olusturulurken problem oldu")
                finally:
                    ticket_list.append(ticket)

        
        else:
            try:
                ticket = Ticket(event=event, user=request.user)
                ticket.save()
                ticket_list.append(ticket)
            except:
                print("ticket olustururken bir hata oldu")

           

        total_cost = 0

        price = event.price  # bunu ticket ya da eventten cekmeliyiz
        if int(count) > 1:
            total_cost = event.price * int(count)
        else:
            total_cost = event.price

        return render(request, 'events/buy_ticket.html', {'total_cost':total_cost, 'ticket_list':ticket_list})

    return redirect('home')


def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.user.is_authenticated:
        ticket.delete()
        messages.success(request, ("Ticket Cancelled!!"))
        return redirect('my_tickets')      
    else:
        messages.success(request, ("You Aren't Authorized To Delete This Event!"))
        return redirect('my_tickets')  


 #buy ticket htmlinde usera fiyat ve info göster / ödemen alındı sayfasına gönderebilirsin,kredi kartı sayfası



 #def buy_ticket2(request):


   
    
     #context = { }
     #return render(request,'events/buy_ticket2.html', context)


   
                 




    
       




