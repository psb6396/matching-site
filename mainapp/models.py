from django.contrib.auth.models import AbstractUser
from django.db import models
    

class Gym(models.Model):
    gym_name = models.CharField(max_length=50, default=None)
    

class My_user(AbstractUser):
    ROLES = (
        ('player', 'Player'),
        ('referee', 'Referee'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='player')
    score = models.IntegerField(default=1000)
    intention_to_fight = models.BooleanField(default=False)
    gym = models.ManyToManyField(Gym) # 관장이 아닌 일반 플레이어들은 어떻게 해줘야하나? null = True같은걸 해줘야하나?
    wins = models.IntegerField(default=0)
    losses =  models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    rank = models.CharField(max_length=50, default=None, null=True)
    elo = models.IntegerField(default = 1000)
    
    def calculate_rank(self) -> None:
        """Calculate the rankings of a player if rankings are enabled."""
        if self.elo >= 2400:
            self.rank = "Grand Master"
        elif self.elo >= 2000:
            self.rank = "Master"
        elif self.elo >= 1850:
            self.rank = "Diamond"
        elif self.elo >= 1650:
            self.rank = "Platinum"
        elif self.elo >= 1500:
            self.rank = "Gold"
        elif self.elo >= 1300:
            self.rank = "Silver"
        elif self.elo >= 1100:
            self.rank = "Bronze"
        else:
            self.rank = "Iron"
    
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
