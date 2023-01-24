from django.shortcuts import render
from .models import My_user
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

# 매칭 잡기 함수?  친구신청수락 알고리즘 공부가 필요할 듯 그걸로 매칭함수 만들수있을듯
#def match_making(request):
#    if 'username' in request.session:
#        
#        my_name = request.session["username"]
#        me = My_user.objects.get(username = my_name)
#        me.intetion_to_fight = True
#        me.save()
#        max_id = My_user.objects.all().aggregate(max_id = Max("id"))['max_id']
#        pk = random.randint(1, max_id)
#        opponent_player = My_user.objects.get(id = pk)
#        
#        if opponent_player.intetion_to_fight is True:

            #먼저 상대방에게 내가 매칭신청한것을 알려야 함 그걸보고 상대방이 최종승낙을 해야지
            # 상대방도 싸우고 싶으면 그다음에는? 뭐해야하지? 싸움 성립시켜야지
#아니다 그전에 유저 프로필부터 만들자 그래야 신청받은사람이 승낙할수있음 ㅇㅇ

@login_required
def profile(request):
    








#    if "username" in request.session:
#        player_1 = My_user(username = "username") #본인 세션을 이용해서 만들고싶은데 어떻게 해야하지??
#       max_id = My_user.objects.all().aggregate(max_id = Max("id"))['max_id']
#        pk = random.randint(1, max_id)
#        player_2 = My_user.objects.get(pk = pk)
# 주석 처리된 부분은 매칭잡을때보다는 매칭뜨고 나서 결과만들어질때 쓰여질 듯
