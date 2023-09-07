from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from .models import My_user, Match
from datetime import datetime, timedelta
from django.http import Http404
from django.contrib import messages

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
        My_user.objects.create_user(password = password, username = username, role='referee')
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
        context = {'me' : me, 'me_referee' : me}
    else:
        context = {'me' : me}
    return render(request, 'mainapp/profile.html', context)


@login_required
def match_make(request):
    me = request.user
    now = datetime.now()
    max_date = now + timedelta(days = 7)
    context = {'now' : now, 'max_date' : max_date}
    if request.method == 'POST':
        date = request.POST.get('gym_date')
        time = request.POST.get('gym_time')
        try:
            confirm_repetition = Match.objects.get(date = date , time=time)
        except Match.DoesNotExist:
            confirm_repetition = None
        if (confirm_repetition == None):
            created_match = Match(date = date, time = time )
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
    me = request.user
    player1 = My_user.objects.get(pk = me.id)
    player1.intention_to_fight = True
    player1.save()
    random_opponent = My_user.objects.exclude(Q(pk = player1.id) | Q(intention_to_fight = False))
    
    if Match.objects.filter(Q(pk = match_id) & Q(player = me)).exists():  #중복확인
        messages.warning(request, "중복입니다.다른 시간대를 선택해주세요.")
        return redirect('mainapp:match_request_page')
    elif random_opponent.exists():
        player2 = random.choice(random_opponent) 
        chosen_match = Match.objects.get(pk = match_id) # 원래 있던 매치를 가져와야하는데 이거맞나
        chosen_match.player.add(player1, player2)
        chosen_match.save()
        return redirect('mainapp:match_request_page')
    elif not random_opponent:
        
    

# def define_winner(request): #
#     me = request.user
#     player1 = My_user.objects.get(pk = me)
    
#     if request.method == 'GET':
#         match_id = request.GET.get('id')
#         match = Match.objects.get(pk = match_id)
#         context = {'match' : match}
        
    #get으로 얻은 match 정보로
    # 누가 승자인지 접근하기 위해 Match 클래스에서 접근??해야하나
    # # referee 입장에서 경기시간 제공하는 html