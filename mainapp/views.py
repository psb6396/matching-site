from django.shortcuts import render
from .models import My_user, Match
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta



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
        created_match = Match(time = time, date = date)
        created_match.save()
        return render(request, 'mainapp/gym_time.html', context)
    else:    
        return render(request, 'mainapp/gym_time.html', context)
    

#매칭 잡기 함수
# def match_request(request):
#     if request.user.is_authenicated:
#         # me = My_user.objects.get(pk = request.user.pk)
#         me = request.user
#         me_player = Player.objects.get(my_users = me)
#         player_that_doesnt_fight = Player.objects.exclude(my_users = me).exclude(intention_to_fight = False)
#         if (random_opponent_player != None):
#             random_opponent_player = random.choice(player_that_doesnt_fight)
#             match = Match.objects.create()
#             match.player.add(me_player, random_opponent_player)
#             # 추가해야할 코드 : 매치에 레프리정보도 담겨야 됨.
#         else:
#             return render(request, 'mainapp/index.html', {'error': 'there is no opponent'})
            #상대없으면 상대 없다는 메세지 띄우고 홈페이지 돌아가기

# def match_making(request):
    
#     # referee가 제공하는 매칭 시간정보? 에 대한 내용?
#     # 위에 아예 매칭관련함수를 싹 바꿔야 할 수도 있음.
# def define_winner(request):
#     referee_verify = isinstance(request.user, Refree)
#     if (referee_verify == True):
        # 누가 승자인지 접근하기 위해 Match 클래스에서 접근??해야하나
        
# referee 입장에서 경기시간 제공하는 html 



