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
        response = render(request, 'mainapp/index.html', {'username': username})
        response.set_cookie('username',username)
        return response
    else:
        messages.error(request, 'invalid login')
        return render(request, 'mainapp/index.html')

#로그아웃 함수 구현하기    
def logout_request(request):
    logout(request)
    return render(request, 'mainapp/index.html')

#페이지마다 로그인되었을때를 다르게 구현해야하는데 
# 세션 이용????

# 이유정 4321