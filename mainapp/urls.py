from django.urls import path
from . import views
 
app_name = "mainapp"

urlpatterns = [
    path('', views.index, name='index' ),
    path('player_register/', views.player_register, name = 'player_register'),
    path('referee_register/', views.referee_register, name = 'referee_register'),
    path('profile/', views.profile, name = 'profile'),
    path('login_request/', views.login_request, name= "login"),
    path("logout_request/", views.logout_request, name= "logout"),
    path("match_make/", views.match_make, name = 'match_make')
#    path("match_making/", views.match_making, name= "match_making"),
]
