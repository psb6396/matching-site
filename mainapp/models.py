from django.contrib.auth.models import AbstractUser
from django.db import models


class My_user(AbstractUser):
    ROLES = (
        ('player', 'Player'),
        ('referee', 'Referee'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='player')
    score = models.IntegerField(default=1000)
    intention_to_fight = models.BooleanField(default=False)
    gym = models.CharField(max_length=50)
    available_time = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)