from django.urls import path
from . import views
from .views import TicketList

urlpatterns = [
    path('', views.home, name="home"),
    path('events/list_events', views.list_events, name="list_events"),
    path('show_event/<event_id>', views.show_event, name="show_event"),
    path('add_event', views.add_event, name="add_event"),
    path('delete_event/<event_id>', views.delete_event, name="delete_event"),
    path('list_eventholder_events', views.list_eventholder_events, name="list_eventholder_events"),
    path('events/ticket_list', TicketList.as_view(), name='ticket_list'),
    #path('events/booking_list', BookingList.as_view(), name='booking_list'),
    #path('book', views.BookingView, name='booking_view'),{}
    path('update_event/<event_id>', views.update_event, name='update_event'),
    path('my_tickets', views.my_tickets_view, name='my_tickets'),
    path('buy_ticket/<event_id>', views.buy_ticket, name='buy_ticket'),
    # path('buy_ticket2', views.buy_ticket2, name='buy_ticket2'),
    path('delete_ticket/<ticket_id>', views.delete_ticket, name="delete_ticket"),
    path('checkout', views.checkout_view, name="checkout"),
    path('buy_ticket_info', views.buy_ticket_info, name="buy_ticket_info"),
    path('add_money', views.add_money, name="add_money"),
    
]
