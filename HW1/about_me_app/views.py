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
                <p> <strong>перейти на страницу проекта </strong>
                    <a href="http://127.0.0.1:8000"><strong>my_project</strong></a>.
                </p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')
    return HttpResponse(page_main)


def about_me(request):
    page_about_me = """
        <div>
            <h1>Страница о себе</h1>
            <img src="https://avatars.mds.yandex.net/i?id=7d7382921eceffaa12e807a55278256c1b2fc273-9869754-images-thumbs&n=13">
            <div class="text">
                <p>
                    В самый морочный час<span style="margin-right:-0.2em;">,
                    </span><span style="margin-left:0.2em;"> </span><br>
                    Если не продохнуть&nbsp;— <br>
                    Радуюсь мелочам. <br>
                    Радуюсь по чуть-чуть. 
                </p>
                <p>
                    Солнечному лучу<span style="margin-right:-0.2em;">,
                    </span><span style="margin-left:0.2em;"> </span><br>
                    Вечеру при свечах. <br>
                    Очень уж я хочу <br>
                    Сердце не удручать. 
                </p>
                <p>
                    Ягодам на снегу<span style="margin-right:-0.2em;">,
                    </span><span style="margin-left:0.2em;"> </span><br>
                    Шишечкам на ольхе <br>
                    Радуюсь<span style="margin-right:-0.2em;">,</span><span style="margin-left:0.2em;"> </span>как могу<span style="margin-right:-0.2em;">,</span><span style="margin-left:0.2em;"> </span><br>
                    Всяческой чепухе. 
                </p>
                <p>
                    Падает жёлудь&nbsp;— «вжух!»&nbsp;— <br>
                    За отворот плаща… <br>
                    Радости нахожу <br>
                    В самых простых вещах. 
                </p>
                <p>
                    Музыке по утрам<span style="margin-right:-0.2em;">,
                    </span><span style="margin-left:0.2em;"> </span><br>
                    Осени волшебству <br>
                    Радуюсь<span style="margin-right:-0.2em;">,</span><span style="margin-left:0.2em;"> </span><br>
                    Как дурак<span style="margin-right:-0.2em;">,</span><span style="margin-left:0.2em;"> </span><br>
                    Факту<span style="margin-right:-0.2em;">,</span><span style="margin-left:0.2em;"> </span>что я живу.
                </p>
            </div>
       </div>
       <form action='http://127.0.0.1:8000/main/' target="_blank">
            <button>Главная страница</button>
        </form>
        <br>
        <footer>
            <div>
                <p> <strong>перейти на страницу проекта </strong>
                    <a href="http://127.0.0.1:8000"><strong>my_project</strong></a>.
                </p>
            </div>
        </footer>
        """
    logger.info(f'Страница "О себе" успешно открыта')
    return HttpResponse(page_about_me)