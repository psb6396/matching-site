from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import My_user

class PlayerRegistrationForm(UserCreationForm):
    class Meta:
        model = My_user
        fields = ('username', 'password1')

class RefereeRegistrationForm(UserCreationForm):
    class Meta:
        model = My_user
        fields = ('username', 'password1')
