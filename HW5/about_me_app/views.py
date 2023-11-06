from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)                # переменная для логирования

def main(request):
    page_main = """
        <div>
            <h1>Главная страница</h1>
            <h2>Домашнее задание к уроку №1:</h2>
            <p>Создайте пару представлений в вашем первом приложении:</p>
            <ul>
                <li>главная</li>
                <li>о себе</li>
            </ul>
            <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.</p>
            <p>Сохраняйте в логи данные о посещении страниц.</p>
        </div>
        <form action='http://127.0.0.1:8000/about_me/' target="_blank">
            <button>О себе</button>
        </form>
        <br>
        <footer>
            <div>
                <p> Контакты: </p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')
    return HttpResponse(page_main)


def about_me(request):

    logger.info(f'Страница "О себе" успешно открыта')
    #return HttpResponse(page_about_me)
    return render(request, 'about_me_app/about_me.html')