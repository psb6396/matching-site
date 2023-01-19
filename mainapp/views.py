from django.shortcuts import render
from .models import My_user
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max
import random

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
def match_making(request):
    me = My_user(username = "username")
    me.
    max_id = My_user.objects.all().aggregate(max_id = Max("id"))['max_id']
    pk = random.randint(1, max_id)
    opponent_player = My_user.objects.get(pk = pk)

    if opponent_player. is True:



#    if "username" in request.session:
#        player_1 = My_user(username = "username") #본인 세션을 이용해서 만들고싶은데 어떻게 해야하지??
#       max_id = My_user.objects.all().aggregate(max_id = Max("id"))['max_id']
#        pk = random.randint(1, max_id)
#        player_2 = My_user.objects.get(pk = pk)
# 주석 처리된 부분은 매칭잡을때보다는 매칭뜨고 나서 결과만들어질때 쓰여질 듯,,
