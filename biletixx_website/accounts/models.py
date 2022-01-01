from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class User(AbstractUser):
    is_registereduser = models.BooleanField(default=False)
    is_eventholder = models.BooleanField(default=False)
    #user = User.objects.get(id=user_id)

class RegisteredUser(models.Model): # store info related to registereduser
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')

   