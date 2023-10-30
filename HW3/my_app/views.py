from django.shortcuts import render

from django.http import HttpResponse



def index(request):
    page_index = '''
        <ul>
            <li><a href="http://127.0.0.1:8000/about_me/">О себе</a></li>
            <li><a href="http://127.0.0.1:8000/shop/main">Интерент магазин </a></li>
            
        </ul>
        <br>
        <footer>
            <div>
                <p> <strong>скачать проект с </strong>
                    <a href="https://github.com/AleksNest/Django_project.git"><strong>gitHub</strong></a>.
                </p>
            </div>
        </footer>
    
    '''
    return HttpResponse(page_index)

