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
    # available_time = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    # match = models.ForeignKey(Match, on_delete=models.CASCADE)
    
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
    date = models.DateField()
    my_user = models.ManyToManyField(My_user)