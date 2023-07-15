from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Player, Referee

class PlayerAdmin(UserAdmin):
    list_display = (
        'username', 'password'
        )
    
class RefereeAdmin(UserAdmin):
    list_display = (
        'username', 'password'
    )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Referee, RefereeAdmin)