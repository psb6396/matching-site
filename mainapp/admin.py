from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Player

class PlayerAdmin(UserAdmin):
    list_display = (
        'username', 'password', 'is_referee'
        )

admin.site.register(Player, PlayerAdmin)
