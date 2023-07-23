from django.contrib.auth.models import AbstractUser
from django.db import models

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
    # 그럼 날짜는? 어떻게?
    date = models.DateField()
    # 따로 views.py 에서 신규객체 create할때 포인트를 줘야할듯

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
    match = models.ForeignKey(Match, on_delete=models.CASCADE)