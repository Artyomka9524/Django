from random import choice, randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

import logging
from .forms import GameForm, GAMES          #импортируем данные из forms.py

logger = logging.getLogger(__name__)


def coins(request: HttpRequest, count: int) -> HttpResponse:
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(("Орел", "Решка"))
    context = {"title": "Все выпавшие варианты Орла и Решки", "res": res}
    return render(request, template_name="games2_app/game.html", context=context)


def cube(request, count: int) -> HttpResponse:
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(("Один", "Два", "Три", "Четыре", "Пять", "Шесть"))
    context = {"title": "Все выпавшие варианты Кубика", "res": res}
    return render(request, template_name="games2_app/game.html", context=context)


def random_number(request, count: int) -> HttpResponse:
    res = {}
    for num in range(1, count + 1):
        res[num] = randint(1, 100)
    context = {"title": "Все случайные числа", "res": res}
    return render(request, template_name="games2_app/game.html", context=context)


# создаем представление для формы,
def game_form(request) -> HttpResponse:
    if request.method == "POST":
        form = GameForm(request.POST)               #создание формы
        title = "Error"
        if form.is_valid():                         #проверка на валидность
            game = form.cleaned_data["game"]        #извлечение из формы данных названия игры, например 'C' - игра coins
            attempts = form.cleaned_data["attempts"] #извлечение из формы данных кол попыток
            logger.info(f"Recieved {game}, {attempts}")

            #1 способ перенаправления на другой адрес
            if game == 'C':
                return coins(request, attempts)
            if game == 'B':
                return cube(request, attempts)
            if game == 'N':
                return random_number(request, attempts)

            # 2 способ перенаправления
            # for name in GAMES:
            #     if game == name[0]:     #если равно какой то игре
            #         return redirect(to=name[1].lower(), count=attempts)
            #         #переадресуем на адрес to (это name в url, например,  'name="coins') = name[1].lower(), например  "coins/10"
    else:
        form = GameForm()               #пустая форма
        title = "Choose the game"
    context = {"title": title, "form": form}

    return render(request, template_name="games2_app/index.html", context=context)