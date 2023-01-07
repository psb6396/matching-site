from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import My_user

class My_userAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff'
        )

admin.site.register(My_user, My_userAdmin)
