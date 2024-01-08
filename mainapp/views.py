from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from .models import My_user, Match, Gym
from datetime import datetime, timedelta
from .elo_system import EloSystem

def index(request):
    return render(request, 'mainapp/index.html')

def player_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        My_user.objects.create_user(password = password, username = username, role='player')
        return render(request, 'mainapp/index.html')
    else:
        return render(request, 'mainapp/player_register.html')


def referee_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        gym_name = request.POST.get('gym_name')
        name_of_gym = Gym(gym_name = gym_name)
        My_user.objects.create_user(password = password, username = username, role='referee', gym = name_of_gym)
        return render(request, 'mainapp/index.html')
    else:
        return render(request, 'mainapp/referee_register.html')

#로그인 함수
def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password) 
    if user is not None:
        login(request, user)
        print("login_success")
        return render(request, 'mainapp/index.html')
    else:
        print("login error or authenticate error")
        return render(request, 'mainapp/index.html')

#로그아웃 함수
def logout_request(request):
    logout(request)
    return render(request, 'mainapp/index.html')

@login_required
def profile(request):
    me = request.user
    if (me.role == 'referee'):
        context = {'me' : me, 'me_referee' : me} # 첫번째 me는 빼도 되지 않나....?
    else:
        context = {'me' : me}
    return render(request, 'mainapp/profile.html', context)


@login_required
def match_make(request):
    referee = request.user #심판
    now = datetime.now()
    max_date = now + timedelta(days = 7)
    context = {'now' : now, 'max_date' : max_date}
    if request.method == 'POST':
        date = request.POST.get('gym_date')
        time = request.POST.get('gym_time')
        if not Match.objects.filter(date = date , time = time, referee = referee).exists():
            created_match = Match(date = date, time = time)
            created_match.save()
            created_match.referee.add(referee)
            created_match.save()
        else:
            print("object_repetition")
        return render(request, 'mainapp/gym_time.html', context)
    else:
        return render(request, 'mainapp/gym_time.html', context)
    
@login_required
def match_request_page(request):
    # matches = Match.objects.all().order_by('date', 'time') 어떻게 렌더링 될지 모르니깐
    matches = Match.objects.all().order_by('date')
    context = {'matches' : matches}
    return render(request, 'mainapp/match_request.html', context) 

@login_required
def match_request(request, match_id):
    player1 = request.user #me
    player1.intention_to_fight = True
    player1.save()
    random_opponent = My_user.objects.exclude(Q(pk = player1.id) | Q(intention_to_fight = False))
    
    if Match.objects.filter(Q(pk = match_id) & Q(player = player1)).exists():  #클릭한 경기에 대한 match_id 중복확인
        print("중복입니다.다른 시간대를 선택해주세요.")
        return redirect('mainapp:match_request_page')
    elif random_opponent.exists():
        player2 = random.choice(random_opponent) 
        chosen_match = Match.objects.get(pk = match_id) 
        chosen_match.player.add(player1, player2)
        chosen_match.save()
        return redirect('mainapp:index')
    elif not random_opponent:
        print("매칭 상대방이 없습니다.")
        return redirect('mainapp:index')
    
def match_info(request): 
    referee = request.user
    matches = Match.objects.filter(referee = referee) # referee의 매치 정보를 불러와야 함
    context = {'matches' : matches}
    return render(request, 'mainapp/referee_match.html', context)
    # matches가 
    # get으로 얻은 match 의 player 정보 불러오기
    # referee 입장에서 경기시간 제공하는 html

def define_winner(request, user_id, match_id, draw): # 클릭한 정보가 winner 고로 loser만 찾아주면 됨.
    match = Match.objects.get(pk = match_id)
    loser = match.player.filter(~Q(pk = user_id))
    elo = EloSystem()
    if (draw == 'false'):
        elo.record_match(winner_id = user_id, loser_id = loser.id, draw = False)
    elif (draw == 'true'):
        elo.record_match(winner_id = user_id, loser_id = loser.id, draw = True)
    
    # 해야할거 : 경기 진행하는 코드???, 