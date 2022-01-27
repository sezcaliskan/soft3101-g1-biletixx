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
from accounts.models import Address, RegisteredUser
import _datetime
from _datetime import timedelta


def check_expiration(event):
    today = _datetime.date.today()

    if event.date < today: #if the event date has past
        return True  # event has expired
    else:
        return False # event has not expired



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
    today = _datetime.datetime.today()
    today=_datetime.datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S.%f')

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = request.user # logged in user
            if check_expiration(event) is True:
                messages.success(request, ("You cant add an event with a past date!!!"))
                return redirect('list_eventholder_events')  
            elif event.date> (today.date()+timedelta(days=365)): #eklenen eventin tarihi bugünün tarihinden maks 1 yıl ilerde olabilir
                messages.success(request, ("eklenecek event tarihi bugünün tarihinden maks 1 yıl ilerde olabilir!!!"))
                return redirect('list_eventholder_events')

            else:  
                form.save()
                return HttpResponseRedirect('list_eventholder_events')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})
    

#co author added

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    tickettobedeleted = Ticket.objects.filter(event=event)
    
    #usersthatboughtthetciket=tickettobedeleted.user

    

    
    if request.user == event.manager:
        if check_expiration(event) is True:  
           messages.success(request, ("This event has expired! You can't delete it!!"))
           return redirect('list_eventholder_events')
        else:
            for i in tickettobedeleted:
                userr=i.user
                print("delete_event---user:{}".format(userr))
                atama=RegisteredUser.objects.filter(user=userr)
                print("delete_event---atama:{}".format(atama))
                reguserforwallet=RegisteredUser.objects.get(user=userr)
                moneyatwallet=reguserforwallet.wallet_money
                #print("delete_event---atama.wallet_money:{}".format(atama.wallet_money))
                #atama.wallet_money.update(10)
                atama.update(wallet_money=moneyatwallet+i.event.price)
                #atama.wallet_money+i.event.price
            
            
            print('Out of loop')
            event.delete()

            messages.success(request, ("Event Deleted!!"))
            return redirect('list_eventholder_events')      
    else:
        messages.success(request, ("You Aren't Authorized To Delete This Event!"))
        return redirect('list_eventholder_events')  
  



def update_event(request, event_id):
    today = _datetime.datetime.today()
    today=_datetime.datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S.%f')
    event = Event.objects.get(pk=event_id)
    eventdatebefore = event.date
    if check_expiration(event) is True: #if event is expired
        messages.success(request, ("This event has expired! You can't edit it!!"))
        return redirect('list_eventholder_events') 
    else: #if event is NOT expired
        form = EventForm(request.POST or None, instance=event)
        if form.is_valid(): #form validse
            if event.date> (eventdatebefore+timedelta(days=10)): #kontrol1 #burdaki event.date formda yeni yazılmış olan
                 messages.success(request, ("You cant edit an event to be more than 10 days late!!"))
                 return redirect('list_eventholder_events')

           
            #elif check_expiration(event) is True: #kontrol2
                #messages.success(request, ("You cant edit an event to be at a passed date!!"))
                #return redirect('list_eventholder_events')  

            elif event.date<eventdatebefore:
                messages.success(request, ("event tarihi güncel tarihten daha geri alınamaz!!"))
                return redirect('list_eventholder_events') 

            
            else:
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

def add_money(request):

    submitted = False

    if request.method == "POST":

        reguserforwallet=RegisteredUser.objects.get(user=request.user)

        reguserforupdate=RegisteredUser.objects.filter(user=request.user)

        moneyatwallet=reguserforwallet.wallet_money

        add_amount = request.POST.get('add_amount') 
    
        #add_amount = 1
        updatedmoney=moneyatwallet + int(add_amount)

        reguserforupdate.update(wallet_money=updatedmoney)

        messages.success(request, ("Money is added!!"))


        return render(request, 'events/home.html', {})

    else:
        if 'submitted' in request.GET:
            submitted = True

        
    return render(request, 'events/add_money.html', {'submitted':submitted}) 



def buy_ticket(request, event_id=None):

    print("hello ticket, i will purchase you")
    print("buy_ticket---user{}".format(request.user))
    
    if request.user.is_eventholder:
        messages.success(request, ("eventholder cant buy ticket!")) 
        return redirect('list_events')

    if request.user.is_superuser:
        messages.success(request, ("admin cant buy ticket!")) 
        return redirect('list_events')

    reguserforwallet=RegisteredUser.objects.get(user=request.user)
    moneyatwallet=reguserforwallet.wallet_money
    reguserforupdate=RegisteredUser.objects.filter(user=request.user)
    
   

    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login') 

   
    count = request.POST.get('count') #alınacak bilet sayısı

    #### sonradan silinecek asagidaki satir
    #count = 1

    print("event id {}".format(event_id))
    event = get_object_or_404(Event, pk=int(event_id))

    if event is None:
        return redirect('home')

    if check_expiration(event) is True:
        messages.success(request, ("Event has expired! You can't buy a ticket!")) 
        return redirect('list_events')

    ticket_list = []
    
    #satılmış biletlerin sayısı
    numOfSoldTickets = Ticket.objects.filter(event=event).count()
    #etkinliğin maksimum kapasitesi
    maksKapasite = event.max_sellable_tickets
    #etkinliğin müsait bilet sayısı
    availableCapacity = maksKapasite-numOfSoldTickets
    
    #uygun bilet sayısından fazla bilet almak isterse
    if int(count)>availableCapacity:
        print(" uygun bilet yok :(")
        messages.success(request, ("Not enough of tickets!")) 
        return redirect('list_events')

    else:

         #birden fazla bilet almak isterse
        if int(count) > 1:

            for i in range (0, int(count)):
                try: 
                    ticket = Ticket(event=event, user=request.user)
                    if moneyatwallet<ticket.event.price*int(count):
                        messages.success(request, ("you dont have enough money"))
                        return render(request, 'registration/profile.html')
                    else:

                        ticket.save()
                        reguserforupdate.update(wallet_money=moneyatwallet-ticket.event.price*int(count))
                        
                except:
                    print("ticket olusturulurken problem oldu")
                finally:
                    ticket_list.append(ticket)

            messages.success(request, ("you bought the ticket! wallet money is reduced"))

        else:
            try:
                ticket = Ticket(event=event, user=request.user)
                if moneyatwallet<ticket.event.price:
                    messages.success(request, ("you dont have enough money"))
                    return render(request, 'registration/profile.html')
                else:

                    ticket.save()
                    reguserforupdate.update(wallet_money=moneyatwallet-ticket.event.price)
                    messages.success(request, ("you bought the ticket! wallet money is reduced"))
                    ticket_list.append(ticket)
            except:
                print("ticket olustururken bir hata oldu")

           

        total_cost = 0

        price = event.price  # bunu ticket ya da eventten cekmeliyiz
        if int(count) > 1:
            total_cost = event.price * int(count)
        else:
            total_cost = event.price

        return render(request, 'events/buy_ticket_info.html', {'availableCapacity':availableCapacity, 'total_cost':total_cost, 'ticket_list':ticket_list})

    print("iflere giremedim")
    return redirect('home')


def delete_ticket(request, ticket_id): #cancel ticket function
    ticket = Ticket.objects.get(pk=ticket_id)
    reguserforwallet=RegisteredUser.objects.get(user=request.user)

    reguserforupdate=RegisteredUser.objects.filter(user=request.user)
    
    ticketprice=ticket.event.price
    moneyatwallet=reguserforwallet.wallet_money
   
    if check_expiration(ticket.event) is False: #if event is not expired
        ticket.delete()
        reguserforupdate.update(wallet_money=ticketprice+moneyatwallet)
        messages.success(request, ("Ticket Cancelled!! Your money is returned!")) #you can cancel it
        return render(request, 'events/home.html')      
    else: #else if event is expired
        messages.success(request, ("This event has already expired, you can't cancel your ticket!")) #you CANT cancel it
        return redirect('my_tickets')  


 #buy ticket htmlinde usera fiyat ve info göster / ödemen alındı sayfasına gönderebilirsin,kredi kartı sayfası





def checkout_view(request):
    me = request.user.id
    address_list = Address.objects.filter(addressowner=me)
    context = { 'address_list':address_list }
    return render(request, 'registration/profile.html')


def buy_ticket_info(request):
    
    context = {  }
    return render(request,'events/home.html', context)
    
                 




    
       




