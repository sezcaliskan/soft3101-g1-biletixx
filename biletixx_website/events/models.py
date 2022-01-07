from django.db import models
from accounts.models import User
from django.conf import settings
#from django.contrib.auth import get_user_model

class Event(models.Model):
    EVENTTYPE = (
                   ('Concert', 'Concert'),
                   ('StageShow', 'StageShow'),
                   ('Movie', 'Movie'),
                   ('Theatre', 'Theatre'),
                   ('Sport', 'Sport'),
                   ('Musical', 'Musical'),


                   )

    EVENTPLACE = (
                   ('Istanbul', 'Istanbul'),
                   ('Ankara', 'Ankara'),
                   ('İzmir', 'İzmir'),
                   ('Eskişehir', 'Eskişehir'),
                   ('Edirne', 'Edirne'),
                   ('Antalya', 'Antalya'),
                   )

    EVENTDATE = (
                   ('Today', 'Today'),
                   ('NextWeek', 'NextWeek'),
                   )
    
    

    
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200, null=True, choices=EVENTPLACE)
    eventtype = models.CharField(max_length=200, null=True, choices=EVENTTYPE)
    date = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)
    venue = models.CharField(max_length=100,null=True)
    hour = models.CharField(max_length=100,null=True)
    #User.add_to_class('manager',models.ManyToManyField('self', symmetrical=False))
    #manager = request.user
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    price = models.IntegerField(null=True)
    max_sellable_tickets= models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    #ticketname = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    



    def __str__(self):
        return f'{self.event}  '

    

#class Booking(models.Model):
    #ticket= models.ForeignKey(Ticket,on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    
    
   #def __str__(self):
       # return f'{self.user} has booked {self.ticket}'

   


     






    




