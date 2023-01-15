from django.shortcuts import render
from .models import My_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

