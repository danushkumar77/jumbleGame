# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='start_game'),  # <-- 'start_game' here
    path('play/', views.play, name='play'),
    path('game-over/', views.game_over, name='game_over'),
]
