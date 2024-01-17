from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import My_user, Match

class My_userAdmin(UserAdmin):
    list_display = (
        'username', 'password'
        )
    

admin.site.register(My_user, My_userAdmin)
admin.site.register(Match)
