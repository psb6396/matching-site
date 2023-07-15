from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Player

class PlayerAdmin(UserAdmin):
    list_display = (
        'username', 'password'
        )

admin.site.register(Player, PlayerAdmin)
