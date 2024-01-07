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
    path("match_make/", views.match_make, name = 'match_make'),
    path('match_request/', views.match_request_page, name = "match_request_page"),
    path('match_request/<int:match_id>/', views.match_request, name= "match_request"),
    path('match_info/', views.match_info, name = "match_info_page"),
    path('define_winner/<int:user_id>/<int:match_id>/', views.define_winner, name='define_winner'),
]