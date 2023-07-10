from django.shortcuts import render, redirect
from .models import Player, Match, Referee
from django.contrib.auth import authenticate, login, logout, get_user_model
import random
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'mainapp/index.html')

def register(request):
    return render(request, 'mainapp/register.html')

def player_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Player.objects.create_user(password = password , username = username)
        user.save()
    return render(request, 'mainapp/index.html')

def referee_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        player = Player.objects.create_user(password = password , username = username)
        referee = Referee(user = player)
        referee.save()
    return render(request, 'mainapp/index.html')


#로그인 함수
def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    if (user != None):
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'mainapp/register.html', {'error': 'Invalid username or password.'})

#로그아웃 함수
def logout_request(request):
    logout(request)
    return render(request, 'mainapp/index.html')

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


def profile(request):
    if request.user.is_authenticated:
        me = request.user
        if (me.is_referee == False):
            me_profile = {'me' : me}
            
        elif (me.is_referee == True):
            me_referee = Referee.objects.get(user = me)
            me_profile = {'me_referee' : me_referee,
                          'me' : me
                            }
            
    return render(request, 'profile.html', me_profile)

    #다른곳에서 프로필정보를 만들어야함 그래도 일단은 프로필 정보 띄우기 ㅇㅇ
    #프로필에 있어야 할 거?? 뭐가 있지.. 자기 매칭 잡혔는지를 확인할 수 있어야 함
