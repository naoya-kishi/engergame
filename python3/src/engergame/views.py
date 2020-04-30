from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

def engergame(request):
    return render(request, 'engergame/engergame.html')

def menu(request):
    response = "menu"
    return render(request, 'engergame/menu.html')

def profile(request):
    response = "profile"
    return render(request, 'engergame/profile.html')

def detail(request):
    response = "detail"
    return render(request, 'engergame/detail.html')

def apply(request):
    response = "apply"
    return render(request, 'engergame/apply.html')

def recruit(request):
    response = "recruit"
    return render(request, 'engergame/recruit.html')

def like(request):
    response = "like"
    return render(request, 'engergame/like.html')

def chat(request):
    response = "chat"
    return render(request, 'engergame/chat.html')

def game(request):
    response = "game"
    return render(request, 'engergame/game.html')

def quest_name(request):
    response = "クエスト名"
    return render(request, 'engergame/quest_name.html')
