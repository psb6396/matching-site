from django.contrib.auth.models import AbstractUser
from django.db import models


class My_user(AbstractUser):
    is_refree = models.BooleanField(default=False)
    
class Player(models.Model):
    my_users = models.OneToOneField(My_user,on_delete=models.CASCADE, related_name = "players", primary_key=True)
    score = models.IntegerField(default = 1000)
    intention_to_fight = models.BooleanField(default = False)
    matching_request_from_others = models.BooleanField(default=False)

class Referee(models.Model):
    user = models.OneToOneField(My_user,on_delete=models.CASCADE, primary_key=True)


class Match(models.Model):
    player = models.ManyToManyField(Player, related_name = "Player")
    referee = models.ManyToManyField(Referee, related_name = "Referee")
    # matching_place????
