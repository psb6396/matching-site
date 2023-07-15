from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    score = models.IntegerField(default = 1000)
    intention_to_fight = models.BooleanField(default = False)
    
    
class Referee(AbstractUser):
    gym = models.CharField(max_length=50)
    available_time = models.DateTimeField

# class Match(models.Model):
#     player = models.ManyToManyField(Player, related_name = "Player")
#     referee = models.ManyToManyField(Referee, related_name = "Referee")
#     # matching_place????
