from django.contrib.auth.models import AbstractUser
from django.db import models


class My_user(AbstractUser):
    score = models.IntegerField(default = 1000)
    intetion_to_fight = models.BooleanField(default = False)
#    match_establishment = models.BooleanField(default = False)
    
    # are_you_winner = models.BooleanField(default=True) 이긴거 입력해서 점수 환산할것?? 이렇게 하는 게 맞나

class Profile(models.Model):
    my_user = models.OneToOneField(My_user, on_delete = models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    matching_request_from_others = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username

#class Match(models.Model):
#    match = models.BooleanField(default = False)