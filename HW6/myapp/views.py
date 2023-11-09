from django.http import HttpResponse
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'text': 'Добро пожаловать на мой первый сайт на Django. \
           Это главная страница на которой я написал эту информацию.'
    }
    #logger.info(f'Показана информация: {html}')
    return render(request, 'myapp/index.html', context=context)         # пробрасываем словарь context в  index.html, где ключ text = '...'


def about(request):
    html = "<h1>Это страница обо мне</h1>" \
           "<p>Меня зовут Сергей. Я хочу стать программистом. Для этого постоянно получаю новые знания и пишу код. </p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)
