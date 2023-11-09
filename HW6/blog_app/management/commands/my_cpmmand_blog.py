from django.core.management.base import BaseCommand
from blog_app.models import Author, Article


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')          # считывает с командной строки count - кол записей в табл Authorи записывает в словарь kwargs по ключу count

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')                                     # ЗАПИСЫВАЕТ из СЛОВАРЯ kwargs в переменную

        for i in range(1, count + 1):
            author = Author(name=f'firstname{i}',
                            surname=f'lastname{i}',
                            email=f'email{i}@mail.ru',
                            biography=f'biography{i}',
                            birthday=f'2000-11-23')
            author.save()                                               # сохранение строки в табл в БД
            for j in range(1, count + 1):
                article = Article(title=f'Title{j}',
                                  content=f'description{j}',
                                  publication_date = f'2000-11-23',
                                  author=author,
                                  category=f'category{i}')               # пропускаем поля (столбцы), которые заполняются автоматои или тмеют дефотное значение
                article.save()                                           # сохранение строки в табл в БД


