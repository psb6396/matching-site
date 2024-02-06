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
    path("make_match/", views.make_match, name = 'make_match'),
    path('match_request/', views.apply_match_page, name = "apply_match_page"),
    path('match_request/<int:match_id>/', views.apply_match, name= "apply_match"),
    path('match_info/', views.match_list, name = "match_info_page"),
    path('define_winner/<int:user_id>/<int:match_id>/', views.define_winner, name='define_winner'),
]