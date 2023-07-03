from django.contrib.auth.models import AbstractUser
from django.db import models


class My_user(AbstractUser):
    is_refree = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    
    # user = models.PositiveSmallIntegerField()
class Player(models.Model):
    my_users = models.OneToOneField(My_user,on_delete=models.CASCADE, related_name = "players", primary_key=True)
    score = models.IntegerField(default = 1000)
    intention_to_fight = models.BooleanField(default = False)

class Refree(models.Model):
    user = models.OneToOneField(My_user,on_delete=models.CASCADE, primary_key=True)


class Match(models.Model):
    player = models.ManyToManyField(Player, related_name = "Player")
    referee = models.
    
# class Matching_place(models.Model):
    
# class Profile(models.Model):
#     my_user = models.OneToOneField(My_user, on_delete = models.CASCADE)
#     matching_request_from_others = models.BooleanField(default=False)
#     # avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     # bio = models.TextField()
    