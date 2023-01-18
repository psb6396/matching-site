from django.shortcuts import render
from .models import My_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django_elo_rating import EloRated

def index(request):
    return render(request, 'mainapp/index.html')

def register(request):
    return render(request, 'mainapp/register.html')

def register_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = My_user.objects.create_user(password = password , username = username)
    user.save()
    return render(request, 'mainapp/index.html')

#로그인 함수
def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        request.session["username"] = username
        return render(request, 'mainapp/index.html')
    else:
        return render(request, 'mainapp/index.html')

#로그아웃 함수 구현하기    
def logout_request(request):
    del request.session["username"]
    logout(request)
    return render(request, 'mainapp/index.html')

# 매칭 잡기 함수?
# 일단은 무작위로 상대방 고를까? elorated 내장함수를 쓰긴 해야할 듯 ??

def match_making(request):
    if "username" in request.session:
        player_1 = My_user(username = "username") #본인 세션을 이용해서 만들고싶은데 어떻게 해야하지??
        
        player_2 = My_user()
        
    else: