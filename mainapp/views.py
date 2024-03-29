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
        My_user.objects.create_user(username = username, password = password,  role='player')
        return render(request, 'mainapp/index.html')
    else:
        return render(request, 'mainapp/player_register.html')


def referee_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        gym_name = request.POST.get('gym_name')
        new_gym = Gym(gym_name = gym_name)
        new_gym.save()
        referee = My_user.objects.create_user(password = password, username = username, role='referee')
        referee.gym.add(new_gym)
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
    else:
        print("login error or authenticate error")
    return render(request, 'mainapp/index.html')

#로그아웃 함수
def logout_request(request):
    logout(request)
    return render(request, 'mainapp/index.html')

@login_required
def profile(request):
    # me = request.user
    # if (me.role == 'referee'):
    #     matches = Match.objects.filter(referee = me) # 이건 오히려 profile에 가까움 ㅇㅇ.
    # elif (me.role == 'player'):
    #     matches = Match.objects.filter(player = me)
    # context = {'matches' : matches}
    # if (me.role == 'referee'):
    #     return render(request, 'mainapp/referee_match.html', context)
    # elif (me.role == 'player'):
    #     return render(request, 'mainapp/player_match.html', context)
    me = request.user
    if (me.role == 'referee'):
        context = {'me' : me, 'me_referee' : me} # 첫번째 me는 빼도 되지 않나....?
    else:
        context = {'me' : me}
    return render(request, 'mainapp/profile.html', context)


@login_required
def make_match(request):
    referee = request.user #심판
    now = datetime.now()
    max_date = now + timedelta(days = 7)
    context = {'now' : now, 'max_date' : max_date}
    if request.method == 'POST':
        date = request.POST.get('gym_date')
        time = request.POST.get('gym_time')
        if not Match.objects.filter(date = date , time = time, referee = referee).exists(): # 클릭한 시간대의 경기가 없다면
            created_match = Match(date = date, time = time) # 매치 생성.
            created_match.save()
            created_match.referee.add(referee)
            created_match.save()
        else:
            print("object_repetition")
    return render(request, 'mainapp/gym_time.html', context)
    
@login_required
def match_list(request): # 걍 모든 match list
    matches = Match.objects.all().order_by('date', 'time') # 매치들을 날짜와 시간순으로 정렬
    context = {'matches' : matches}
    return render(request, 'mainapp/apply_match.html', context)
    
@login_required
def detail_of_match(request, match_id):
    match = Match.objects.get(pk = match_id)
    context = {'match' : match}
    return render(request, 'mainapp/detail_of_match.html', context)

@login_required
def apply_match(request, match_id): 
    myself = request.user #me
    match = Match.objects.get(pk = match_id)
    count_of_player = match.player.all().count()
    if (count_of_player == 2): # 한 매칭에 2명이상 있으면 에러 발생.
        print("자리가 없습니다.") 
    elif(count_of_player < 2):
        match.player.add(myself)
    return redirect('mainapp:index')
    
    # player1.intention_to_fight = True
    # player1.save()
    # random_opponent = My_user.objects.exclude(Q(pk = player1.id) | Q(intention_to_fight = False))
    
    # if Match.objects.filter(Q(pk = match_id) & Q(player = player1)).exists():  #클릭한 경기에 대한 match_id 중복확인
    #     print("중복입니다.다른 시간대를 선택해주세요.")
    #     return redirect('mainapp:match_request_page')
    # elif random_opponent.exists():
    #     player2 = random.choice(random_opponent) 
    #     chosen_match = Match.objects.get(pk = match_id) 
    #     chosen_match.player.add(player1, player2)
    #     chosen_match.save()
    # elif not random_opponent:
    #     print("매칭 상대방이 없습니다.")
    
    
def cancel_request(request, match_id):
    myself = request.user
    match = Match.objects.get(pk = match_id)
    match.player.remove(myself)
    return redirect('mainapp:match_list')

def cancel_match(request, match_id):
    myself = request.user
    match = Match.objects.get(pk = match_id)
    match.delete()
    return redirect('mainapp:gym_info')


    

    
def gym_info(request, match_id):
    match = Match.objects.get(pk = match_id)
    gym_instance = match.gym
    context = {'gym_instance' : gym_instance}
    return render(request, 'mainapp/gym_info.html', context)
    # gym_info 함수에서 kakaomap.js 의 adresssearch로 gym의 주소 문자열을 보내줘야 할 듯.

def define_winner(request, user_id, match_id): # 클릭한 정보가 winner 고로 loser만 찾아주면 됨.
    match = Match.objects.get(pk = match_id)
    elo = EloSystem()
    if (user_id == 0): #user의 id 로는 0 이 할당되지 않음을 이용함.
        player_objects = match.player.all()
        player1 = player_objects[0]
        player2 = player_objects[1]
        elo.record_match(winner_id = player1.id, loser_id = player2.id, draw = True) # draw 판정
    else:
        loser = match.player.get(~Q(pk = user_id)) #get 안써도 되나?
        elo.record_match(winner_id = user_id, loser_id = loser.id, draw = False)
    
    return redirect('mainapp:profile')
    
