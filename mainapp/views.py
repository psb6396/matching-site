from django.shortcuts import render, redirect
from .models import My_user, Match, Player
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
    if user is not None:
        login(request, user)
        # request.session["username"] = username
        return redirect('index')
    else:
        return render(request, 'mainapp/index.html', {'error': 'Invalid username or password.'})

#로그아웃 함수
def logout_request(request):
    # del request.session["username"]
    logout(request)
    return render(request, 'mainapp/index.html')

#매칭 잡기 함수
def match_making(request):
    if request.user.is_authenicated:
    # if 'username' in request.session:
        
        # my_name = request.session["username"]
        me = Player.objects.get(username = )
        me.intention_to_fight = True
        me.save()
        user = My_user.objects.exclude(username = my_name).exclude(intention_to_fight = False)
        random_opponent_player = random.choice(user)

        if (random_opponent_player != None):
            match = Match.objects.create(player1 = me , player2 = random_opponent_player)
            match.save()

    
            

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
