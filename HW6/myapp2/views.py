from django.shortcuts import render

from myapp2.models import Article, Author, Comment

# вывод всех статей определенного автора
def get_articles(request, author_id: int):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author.id)
    context = {
        'articles': articles
    }
    return render(request, 'myapp/new.html', context=context)


def detail_article(request, article_id: int):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('-change_at')
    #извлекаются в список qweryset все комментарии определенного автора и сортируется по дате изменения начиная с ноой
    article.count_views += 1                # кол просмотров статьи
    article.save()
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'myapp/detail.html', context=context)




