from django.urls import path
from myapp2 import views

urlpatterns = [
    path('articles/<int:author_id>', views.get_articles, name='articles'),
    path('detail/<int:article_id>', views.detail_article, name='detail_article')
]
