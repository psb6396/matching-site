from django.shortcuts import render, redirect
from .models import My_user, Player, Match, Refree
from django.contrib.auth import authenticate, login, logout, get_user_model
import random
from django.contrib.auth.decorators import login_required
from .forms import PlayerRegistrationForm, RefereeRegistrationForm


def index(request):
    return render(request, 'mainapp/index.html')

def register(request):
    return render(request, 'mainapp/register.html')

def player_registration(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_player = True
            user.save()
            # Additional logic or redirect here
            return redirect('index')  # Redirect to a success page
    else:
        form = PlayerRegistrationForm()
    
    return render(request, 'index.html', {'form': form})

def referee_registration(request):
    if request.method == 'POST':
        form = RefereeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_referee = True
            user.save()
            # Additional logic or redirect here
            return redirect('index')  # Redirect to a success page
    else:
        form = RefereeRegistrationForm()
    
    return render(request, 'referee_registration.html', {'form': form})

#로그인 함수
def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    if (user != None):
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'mainapp/index.html', {'error': 'Invalid username or password.'})

#로그아웃 함수
def logout_request(request):
    # del request.session["username"]
    logout(request)
    return render(request, 'mainapp/index.html')

#매칭 잡기 함수
def match_request(request):
    if request.user.is_authenicated:
        me = My_user.objects.get(pk = request.user.pk)
        me_player = Player(my_users = me, intention_to_fight = True)
        me_player.save()
        player_that_doesnt_fight = Player.objects.exclude(my_users = me).exclude(intention_to_fight = False)
        if (random_opponent_player != None):
            random_opponent_player = random.choice(player_that_doesnt_fight)
            match = Match.objects.create()
            match.player.add(me_player, random_opponent_player)
            # 추가해야할 코드 : 매치에 레프리정보도 담겨야 됨.
        else:
            return render(request, 'mainapp/index.html', {'error': 'there is no opponent'})
            #상대없으면 상대 없다는 메세지 띄우고 홈페이지 돌아가기

def match_making(request):
    
    # referee가 제공하는 매칭 시간정보? 에 대한 내용?
            
def define_winner(request):
    referee_verify = isinstance(request.user, Refree)
    if (referee_verify == True):
        # 누가 승자인지 접근하기 위해 Match 클래스에서 접근??해야하나
        
# referee 입장에서 경기시간 제공하는 html 