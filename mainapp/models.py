from django.contrib.auth.models import AbstractUser
from django.db import models
    
class Gym(models.Model):
    gym_name = models.CharField(max_length=50)

class My_user(AbstractUser):
    ROLES = (
        ('player', 'Player'),
        ('referee', 'Referee'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='player')
    score = models.IntegerField(default=1000)
    intention_to_fight = models.BooleanField(default=False)
    gym = models.ManyToManyField(Gym)

    # 심판과 gym 정보를 연결시켜야 함.

class Match(models.Model):
    time1 = 'time1'
    time2 = 'time2'
    time3 = 'time3'
    time4 = 'time4'
    Time_choices = [
        (time1, 'Time1'),
        (time2, 'Time2'),
        (time3, 'Time3'),
        (time4, 'Time4'),
    ]
    time = models.CharField(max_length=10, choices=Time_choices)
    date = models.DateField(blank= True,null=True,auto_now=False, auto_now_add=False)
    player = models.ManyToManyField(My_user, related_name = 'player_match')
    referee = models.ManyToManyField(My_user,related_name = 'referee_match')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True, default=None)