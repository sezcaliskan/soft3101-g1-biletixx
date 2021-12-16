from django.contrib import admin

from .models import *

admin.site.register(Event)
admin.site.register(Ticket_Class)
admin.site.register(EventTicketSell)

