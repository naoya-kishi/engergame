from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.engergame, name='engergame'),
    path('menu', views.menu, name='menu'),
    path('profile', views.profile, name='profile'),
    path('recruit', views.recruit, name='recruit'),
    path('like', views.like, name='like'),
    path('chat', views.chat, name='chat'),
    path('game', views.game, name='game'),
    path('recruit/detail', views.detail, name='detail'),
    path('recruit/detail/apply', views.apply, name='apply'),
    path('game/クエスト名', views.quest_name, name='quest_name'),
]
