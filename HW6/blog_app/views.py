from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Author, Comment
from .forms import AddAuthorForm, ArticleForm, AddCommentForm


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Главная страница",
        "content": "Чтобы выбрать автора, укажите в адресе его ID (author/id).",
    }
    authors = Author.objects.all()
    context["authors"] = authors
    return render(request, template_name="blog_app/index.html", context=context)

# вывод статей по id автора
def articles_by_author(request: HttpRequest, author_pk: int) -> HttpResponse:
    author = get_object_or_404(Author, pk=author_pk)
    articles = Article.objects.filter(author=author)
    context = {"title": f"Автор {author.full_name}", "articles": articles}
    return render(request, template_name="blog_app/articles_by_author.html", context=context)


def article_full(request: HttpRequest, article_pk: int) -> HttpResponse:
    article = get_object_or_404(Article, pk=article_pk)
    article.views_count()
    comments = article.comments.select_related("author").order_by("-updated_at").all()

    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data["author"]
            author, _ = Author.objects.get_or_create(name=author_name)
            comment = form.cleaned_data["comment"]
            new_comment = Comment.objects.create(
                author=author, comment=comment, article=article
            )
            new_comment.save()
            form = AddCommentForm()
    else:
        form = AddCommentForm()
    context = {
        "article": article,
        "comments": comments,
        "form": form,
    }
    return render(request, template_name="blog_app/article_full.html", context=context)


# для заполнения формы ввода новго автора
def add_new_author(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        message = "Error"
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            email = form.cleaned_data["email"]
            biography = form.cleaned_data["biography"]
            birthday = form.cleaned_data["birthday"]
            author = Author.objects.create(name=name,surname=surname, email=email, biography=biography, birthday=birthday,) # создаем автора

            #author = Author.objects.create(**form.cleaned_data)) # это можно написать вместо строк с 56 по 61

            author.save()   #сохраняем в БД
            return articles_by_author(request, author.pk)
            #return redirect(to="index")   # или можно так: переходим по маршруту, который ищет по имени name в файле urls.py( path("", index, name="index"),  )
    else:
        form = AddAuthorForm()
        message = "Fill fields below"
    context = {"form": form, "message": message}
    return render(request, template_name="blog_app/add_author.html", context=context)


def add_new_article(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ArticleForm(request.POST)
        message = "Error"
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            publication_date = form.cleaned_data["publication_date"]
            author_given_name = form.cleaned_data["author"]
            author, _ = Author.objects.get_or_create(name=author_given_name)
            category = form.cleaned_data["category"]
            is_published = form.cleaned_data["is_published"]
            article = Article.objects.create(
                title=title,
                content=content,
                publication_date=publication_date,
                author=author,
                category=category,
                is_published=is_published,
            )
            article.save()
            return redirect(to="index")
    else:
        form = ArticleForm()
        message = "Fill fields below"
    context = {"form": form, "message": message}
    return render(request, template_name="blog_app/add_article.html", context=context)