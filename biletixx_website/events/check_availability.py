from events.models import Event, Ticket, Booking 


def check_availability(ticket,max_sellable_tickets)
avail_list = []
booking_list = Booking.objects.filter(ticket=ticket)
for booking in booking_list
    if booking.ticket.max_sellable_tickets>0:
	    avail_list.append(True)
    else:
    	avail_list.append(False)
return all(avail_list)