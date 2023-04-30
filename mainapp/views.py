from django.shortcuts import render
from .models import My_user, Match
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max
import random
from django.contrib.auth.decorators import login_required

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

#매칭 잡기 함수
def match_making(request):
    if 'username' in request.session:
        
        my_name = request.session["username"]
        me = My_user.objects.get(username = my_name)
        me.intention_to_fight = True
        me.save()
        user = My_user.objects.exclude(username = my_name).exclude(intention_to_fight = False)
        random_opponent_player = random.choice(user)
        #매치 객체 생성해야함...argument 정보 넣어주기
        match = Match.objects.create(player1 = me , player2 = random_opponent_player)
        match.save()
        #무엇을 해야할까
    
            

@login_required
def profile(request):
    my_name = request.session["username"]
    me = My_user.objects.get(username = my_name)
    me.
    
    # return render(request, 'profile.html')


    if "username" in request.session:
       player_1 = My_user(username = "username")
       max_id = My_user.objects.all().aggregate(max_id = Max("id"))['max_id']
       pk = random.randint(1, max_id)
       player_2 = My_user.objects.get(pk = pk)
