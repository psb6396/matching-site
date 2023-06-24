from django.urls import path
from . import views
 
app_name = "mainapp"

urlpatterns = [
    path('', views.index, name='index' ),
    path('register/', views.register, name = 'register'),
    # path('register_request/', views.register_request, name = 'register_request'),
    path('login_request/', views.login_request, name= "login"),
    path("logout_request/", views.logout_request, name= "logout"),
#    path("match_making/", views.match_making, name= "match_making"),
#    path("profile/", views.profile, name = "profile"),
]
