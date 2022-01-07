from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class User(AbstractUser):
    is_registereduser = models.BooleanField(default=False)
    is_eventholder = models.BooleanField(default=False)
    #user = User.objects.get(id=user_id)

class RegisteredUser(models.Model): # store info related to registereduser
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')

class Address(models.Model):
    COUNTRY = (
                   ('Turkey', 'Turkey'),

                   )

    CITY = (
                   ('Istanbul', 'Istanbul'),
                   ('Ankara', 'Ankara'),
                   ('İzmir', 'İzmir'),
                   ('Antalya', 'Antalya'),
                   )

    
     
    addressname = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=200, null=True, choices=COUNTRY)
    city = models.CharField(max_length=200, null=True, choices=CITY)
    ZIP = models.IntegerField(max_length=100, null=True)
    addressowner =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)


    def _str_(self):
        return f'{self.name}'
   