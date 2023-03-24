from django.contrib.auth.models import AbstractUser
from django.db import models


class My_user(AbstractUser):
    score = models.IntegerField(default = 1000)
    intetion_to_fight = models.BooleanField(default = False)

    

class Match(models.Model):
    player = models.ManyToManyField('My_user', related_name = 'Match')
#   where_to_fight = 
#    match_establishment = models.BooleanField(default = False)
    # are_you_winner = models.BooleanField(default=True) 

class Profile(models.Model):
    my_user = models.OneToOneField(My_user, on_delete = models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    matching_request_from_others = models.BooleanField(default=False)
    

#    def __str__(self):
#        return self.user.username

