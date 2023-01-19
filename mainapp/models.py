from django.contrib.auth.models import AbstractUser
from django.db import models
from django_elo_rating import EloRated


class My_user(AbstractUser, EloRated):
    score = models.IntegerField(default = 1000)
    i_want_to_fight = models.BooleanField(default = False)
    
    # are_you_winner = models.BooleanField(default=True) 이긴거 입력해서 점수 환산할것?? 이렇게 하는 게 맞나

