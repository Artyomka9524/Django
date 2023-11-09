from django.urls import path
from .views import coins, cube, random_number
from .views import game_form

urlpatterns = [
    path("coins/<int:count>", coins, name="coins"),  #вывод случайным образом n попыток выброса монетки
    path("cube/<int:count>", cube, name="cube"),     #вывод случайным образом n попыток выброса стороны куба
    path("random/<int:count>", random_number, name="random_number"),  #вывод случайным образом n раз случайного числа

    path("form/", game_form, name="game_form"),
    # создается форма, где заполняются данны, при нажатии на submit идлет переадресация на соответствующую страничку игры с результатом(стр 6-8)
]