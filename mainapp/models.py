from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    score = models.IntegerField(default = 1000)
    intention_to_fight = models.BooleanField(default = False)
    matching_request_from_others = models.BooleanField(default=False) 
    # 매칭 요청(누가 했는지에 대한 정보는 어떡하지??)   
    is_refree = models.BooleanField(default=False)

class Referee(models.Model):
    user = models.OneToOneField(Player,on_delete=models.CASCADE, primary_key=True)
    

class Match(models.Model):
    player = models.ManyToManyField(Player, related_name = "Player")
    referee = models.ManyToManyField(Referee, related_name = "Referee")
    # matching_place????
