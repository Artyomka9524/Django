from django.urls import path
from .views import (
    index,
    articles_by_author,
    article_full,
    add_new_author,
    add_new_article,
)

urlpatterns = [
    path("", index, name="index"),                  # главная страница
    path("author/<int:author_pk>", articles_by_author, name="articles_by_author"),      # страница для вывода статей определенного автора
    path("article/<int:article_pk>", article_full, name="article_full"),                # страница для вывода статьи с формой для добавления комментария
    path("add_author/", add_new_author, name="add_new_author"),                         # страница для ввода в форму нового автора и сохранения в БД
    path("add_article/", add_new_article, name="add_new_article"),                      # страница для ввода в форму новой статьи существующего автора и сохранения в БД
]