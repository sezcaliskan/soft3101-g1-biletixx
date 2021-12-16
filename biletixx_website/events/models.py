from django.db import models


class Event(models.Model):
    EVENTTYPE = (
                   ('Concert', 'Concert'),
                   ('StageShow', 'StageShow'),
                   )

    EVENTPLACE = (
                   ('Istanbul', 'Istanbul'),
                   ('Ankara', 'Ankara'),
                   )

    EVENTDATE = (
                   ('Today', 'Today'),
                   ('NextWeek', 'NextWeek'),
                   )
    
    

    
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200, null=True, choices=EVENTPLACE)
    eventtype = models.CharField(max_length=200, null=True, choices=EVENTTYPE)
    date = models.CharField(max_length=200, null=True, choices=EVENTDATE)



class Ticket_Class(models.Model):
    price = models.IntegerField()
    ticketname = models.CharField(max_length=100)

    

class EventTicketSell(models.Model):
    event= models.ForeignKey(Event,on_delete=models.CASCADE)
    ticket= models.ForeignKey(Ticket_Class,on_delete=models.CASCADE)
    max_sellable_tickets= models.IntegerField()
    
    def __str__(self):
        return self.event.name

   


     






    




