from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_registereduser = models.BooleanField(default=False)
    is_eventholder = models.BooleanField(default=False)

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')

   