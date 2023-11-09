import random
from django.http import HttpResponse
import logging
from myapp2.models import Coin
from django.shortcuts import render



logger = logging.getLogger(__name__)


def eagle(request):
    game_list = ['орел', 'решка']
    response = random.choice(game_list)
    coin = Coin(is_eagle=response)              # при вызове представления в браузере, возварщается рандомное значение стороны монетки
    coin.save()
    logger.info(f'Значение: {coin}')
    return HttpResponse(coin)


# вывод n последних бросков из табл coin
def show_elements(request, n: int):
    return HttpResponse(f'{Coin.counter(n)}')       # метод counter написан в models.py


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Кубик выпал стороной: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(0, 100)
    logger.info(f'Случайное число: {number}')
    return HttpResponse(number)



def eagle_tmpl(request, count: int):
    game_list = ['орел', 'решка']
    result = []
    for i in range(count):
        response = random.choice(game_list)
        result.append(response)                     #генерируется список рондомных значений орел или решка
    context = {
        'result': result
    }
    return render(request, 'myapp/index.html', context=context)

